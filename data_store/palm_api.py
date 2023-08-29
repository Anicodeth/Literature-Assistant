from ..configurations.palm_configuration import palm, defaults

def get_poem(prompt):
  response = palm.generate_text(
  **defaults,
  prompt= f"Write a poem about '{prompt}'")  
  return response.result


