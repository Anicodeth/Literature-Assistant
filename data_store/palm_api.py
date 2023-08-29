from ..configurations.palm_configuration import palm, defaults

def generate_text(prompt):
  response = palm.generate_text(
  **defaults,
  prompt= prompt)  
  return response.result


