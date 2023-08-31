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
    def get_essay(self, prompt):
        prompt = f"Write an essay about, '{prompt}'."
        result = generate_text(prompt)
        return result
    def get_lyrics(self, prompt):
        prompt = f"Write lyrics about, '{prompt}'."
        result = generate_text(prompt)
        return result
    def get_script(self, prompt):
        prompt = f"Write a script about, '{prompt}'."
        result = generate_text(prompt)
        return result
    def get_dialogue(self, prompt):
        prompt = f"Write a dialogue about, '{prompt}'."
        result = generate_text(prompt)
        return result
    def get_novel(self, prompt):
        prompt = f"Write a novel about, '{prompt}'."
        result = generate_text(prompt)
        return result
    def get_fiction(self, prompt):
        prompt = f"Write a fiction about, '{prompt}'."
        result = generate_text(prompt)
        return result
    def get_nonfiction(self, prompt):
        prompt = f"Write a nonfiction about, '{prompt}'."
        result = generate_text(prompt)
        return result
    
    
