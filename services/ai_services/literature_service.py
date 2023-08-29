from ...data_store.palm_api import generate_text
class LitService:    
    def get_poem(prompt):
        prompt = f"Write a poem about, '{prompt}'."
        result = generate_text(prompt)
        return result
    
