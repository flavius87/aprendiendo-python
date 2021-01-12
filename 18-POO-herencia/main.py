import clases

persona = clases.Persona()
persona.setNombre("Victor")
persona.setApellido("Robles")
persona.setAltura("190 cm")
persona.setEdad("800 años")

print(f"La persona es: {persona.getNombre()} {persona.getApellido()}")
print(persona.hablar())
print("\n----------------------------")
informatico = clases.Informatico()
informatico.setNombre("Carlos")
informatico.setApellido("Martínez")

print(f"El informático es: {informatico.getNombre()} {informatico.getApellido()}")
print(informatico.getLenguajes())
print(informatico.caminar())
print("--------------")

tecnico = clases.TecnicoRedes()
tecnico.setNombre("Manolo")
print(tecnico.auditarRedes, tecnico.getNombre(), tecnico.getLenguajes())