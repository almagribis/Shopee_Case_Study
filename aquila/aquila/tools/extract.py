import base64
import os
from langchain.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from aquila.config import settings

system_prompt = """You are a Food Receipt Extractor Agent.
Your task is to analyze an image of an online food order receipt and extract structured data from it.
Follow these instructions carefully:
- Always return the result in valid JSON format.
- If a field is not available, return an empty string ("").
- Normalize all dates and times into ISO 8601 format (e.g., 2025-10-09T18:44:00).
- Remove currency symbols (e.g., Rp, $, etc.) and keep numeric values only for prices.
- Maintain the exact JSON schema structure below.
```
{
  "order_id": str,                // Booking ID or order number
  "order_time": str,              // ISO format, e.g. 2025-10-09T18:44:00
  "payment_method": str,          // visa, mastercard, ovo, linkaja, gopay, shopeepay, or empty
  "merchant_name": str,           // Merchant or restaurant name
  "platform": str,                // shopeefood, grabfood, gofood, or empty
  "total_initial_price": int,     // Total price before discount
  "total_discount": int,          // Total discount amount
  "total_paid": int,              // Total amount paid
  "items": [
    {
      "item_name": str,
      "item_qty": int
    }
  ]
}
```
Example Response:
```
{
  "order_id": "A12345",
  "order_time": "2025-10-09T18:44:00",
  "payment_method": "gopay",
  "merchant_name": "Bakso Jaya",
  "platform": "gofood",
  "total_initial_price": 45000,
  "total_discount": 5000,
  "total_paid": 40000,
  "items": [
    { "item_name": "Bakso Urat", "item_qty": 1 },
    { "item_name": "Es Teh Manis", "item_qty": 2 }
  ]
}
```
"""

class ExtractReceipt():
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(google_api_key=settings.llm_config.api_key,
                                          model=settings.llm_config.model,
                                          temperature=0,
                                          max_tokens=None,
                                          timeout=None,
                                          max_retries=2)
        
        
    def main(self, encoded_image:str):
        message = HumanMessage(
            content=[
                {"type": "text", "text":system_prompt},
                {"type": "image_url", "image_url": f"data:image/png;base64,{encoded_image}"},
            ]
        )
        result = self.llm.invoke([message])
        return result.content
    
