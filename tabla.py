class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        
    def hash_func(self, key):
        # Convierte la clave en un índice (usa el valor ASCII de cada caracter)
        return sum(ord(char) for char in key) % self.size
    
    def insert(self, key, value):
        index = self.hash_func(key)
        # Verificar si la clave ya existe y actualizar
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # Si no existe, agregarla
        self.table[index].append((key, value))
        
    def search(self, key):
        index = self.hash_func(key)
        for (k, v) in self.table[index]:
            if k == key:
                return v
        return None

    # 🔹 1. Eliminar una clave
    def delete(self, key):
        """Elimina una clave si existe"""
        index = self.hash_func(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False

    # 🔹 2. Mostrar toda la tabla hash
    def display(self):
        """Muestra el contenido completo de la tabla"""
        for i, bucket in enumerate(self.table):
            print(f"Índice {i}: {bucket}")

    # 🔹 3. Calcular el factor de carga
    def load_factor(self):
        """Calcula cuán llena está la tabla (número de elementos / tamaño)"""
        total_elements = sum(len(bucket) for bucket in self.table)
        return total_elements / self.size


# --- Ejemplo de uso ---
tabla = HashTable(10)
tabla.insert("A", 1)
tabla.insert("B", 2)
tabla.insert("C", 3)
tabla.insert("D", 4)
tabla.insert("E", 5)
tabla.insert("F", 6)
tabla.insert("G", 7)
tabla.insert("H", 8)
tabla.insert("I", 9)
tabla.insert("J", 10)

print("🔍 Buscar 'E':", tabla.search("E"))
print("❌ Eliminar 'E':", tabla.delete("E"))
print("🔍 Buscar 'E' después de eliminar:", tabla.search("E"))

print("\n📊 Factor de carga:", tabla.load_factor())
print("\n📋 Contenido de la tabla:")
tabla.display()
