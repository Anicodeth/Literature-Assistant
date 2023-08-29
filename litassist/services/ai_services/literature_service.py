from litassist.data_store.palm_api import generate_text

class LitService:    
    def get_poem(self, prompt):
        prompt = f"Write a poem about, '{prompt}'."
        result = generate_text(prompt)
        return result 
    def get_story(self, prompt):
        prompt = f"Write s story about, '{prompt}'."
        result = generate_text(prompt)
        return result
    
