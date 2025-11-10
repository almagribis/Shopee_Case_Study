import json
from typing import List, Dict, Any, Optional
from calyx.vectordb.helper import cosine_similarity
from calyx.config import settings
"""
with assumption that we can't use any high level library to perform vector databases
operations and queris, I use langchain and huggingface to handle tokenization and embeddings.
"""
from langchain_huggingface import HuggingFaceEndpointEmbeddings

class VectorDB():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        """setup embeddings model"""
        self.embeddings =  HuggingFaceEndpointEmbeddings(
            provider="hf-inference",
            huggingfacehub_api_token=settings.embedding.token,
            model=settings.embedding.model,
            model_kwargs={"normalize": True, "truncate": True}
        )
        self.docs: List[Dict[str, Any]] = []
        self.vectors: List[List[float]] = []
    
    def add_document(self, doc_id:str, text:str, text_col:str, metadata:Optional[Dict[str,Any]]=None):
        if not metadata:
            metadata = {}
        metadata.pop(text_col, None)
        vector = self.embeddings.embed_documents([text])
        self.docs.append({"id":doc_id, "text":text, "metadata":metadata})
        self.vectors.append(vector[0])
    
    def search(self, query:str, top_k:int=3):
        vector_query = self.embeddings.embed_query(query)
        scores = []
        for idx, vec in enumerate(self.vectors):
            score = cosine_similarity(vector_query, vec)
            scores.append((score, idx))
        scores.sort(key=lambda x: x[0], reverse=True)
        result = [
            {
                **self.docs[idx],
                "score":score,
            }
            for score, idx in scores[:top_k]
        ]
        return result
    
    def save(self, path:str):
        data = {"docs":self.docs, "vectors":self.vectors}
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f)
    
    def load(self, path:str):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.docs = data["docs"]
        self.vectors = data["vectors"]
