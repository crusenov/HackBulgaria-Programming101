def magic_string(s):
  """Vryshtame dyljinata na spisyka, v koito dobavqme element, samo ako
  vyv vhodniq string s ima character, koito ne si e na mqstoto"""
  return len([i for i, c in enumerate(s) if i < len(s) // 2 and c == '<'
              or i >= len(s) // 2 and c == '>'])
