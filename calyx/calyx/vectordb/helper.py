import uuid

def create_id(text:str):
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, text))
    
def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def norm(a):
    return sum(x*x for x in a)**0.5

def cosine_similarity(a,b):
    na,nb = norm(a), norm(b)
    return dot(a,b)/(na*nb)