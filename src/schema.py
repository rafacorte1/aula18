from pydantic import BaseModel

class PokemonSchema(BaseModel):
    name: str
    type: str
    
    class ConfigDict:
        from_attributes = True