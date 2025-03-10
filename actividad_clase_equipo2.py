import datetime
from typing import List, Dict

Expense = Dict[str, str]
ExpenseList = List[Expense]

def mostrar_menu() -> None:
    print("\n🌟 Gestión de Gastos 🌟")
    print("1. Agregar gasto")
    print("2. Ver todos los gastos")
    print("3. Resumen por categoría")
    print("4. Reporte mensual")
    print("5. Salir")

def obtener_opcion_valida() -> int:
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if 1 <= opcion <= 5:
                return opcion
            print("⚠️ Opción fuera de rango (1-5)")
        except ValueError:
            print("⚠️ Ingrese un número válido")

def agregar_gasto(gastos: ExpenseList) -> None:
    print("\n📝 Nuevo Gasto")
    categoria = input("Categoría (ej. Comida, Transporte): ").capitalize()
    monto = float(input("Monto: $"))
    fecha = datetime.date.today().strftime("%Y-%m-%d")
    
    nuevo_gasto = {
        'fecha': fecha,
        'categoria': categoria,
        'monto': f"{monto:.2f}"
    }
    
    gastos.append(nuevo_gasto)
    print(f"✅ Gasto de ${monto:.2f} en {categoria} registrado")

def mostrar_gastos(gastos: ExpenseList, titulo: str) -> None:
    print(f"\n📄 {titulo}")
    if not gastos:
        print("No hay registros")
        return
        
    print(f"{'Fecha':<12} | {'Categoría':<15} | {'Monto':>10}")
    print("-" * 45)
    
    for gasto in gastos:
        print(f"{gasto['fecha']:<12} | {gasto['categoria']:<15} | ${gasto['monto']:>10}")

def resumen_categorias(gastos: ExpenseList) -> None:
    categorias = {}
    for gasto in gastos:
        cat = gasto['categoria']
        monto = float(gasto['monto'])
        
        if cat in categorias:
            categorias[cat]['total'] += monto
            categorias[cat]['count'] += 1
        else:
            categorias[cat] = {'total': monto, 'count': 1}
    
    print("\n📊 Resumen por Categoría")
    if not categorias:
        print("No hay datos para mostrar")
        return
    
    for cat, datos in categorias.items():
        print(f"- {cat}: ${datos['total']:.2f} ({datos['count']} gastos)")

def reporte_mensual(gastos: ExpenseList) -> None:
    if not gastos:
        print("\nNo hay gastos registrados")
        return
    
    montos = [float(g['monto']) for g in gastos]
    total = sum(montos)
    promedio = total / len(montos)
    max_gasto = max(montos)
    
    print("\n📈 Reporte Mensual")
    print(f"Total gastado: ${total:.2f}")
    print(f"Promedio diario: ${promedio:.2f}")
    print(f"Gasto más alto: ${max_gasto:.2f}")

def main():
    gastos_ejemplo = [
        {'fecha': '2023-10-01', 'categoria': 'Comida', 'monto': '45.50'},
        {'fecha': '2023-10-02', 'categoria': 'Transporte', 'monto': '15.00'},
        {'fecha': '2023-10-03', 'categoria': 'Entretenimiento', 'monto': '30.00'}
    ]
    
    print("¡Bienvenido a tu Gestor de Gastos!")
    mostrar_gastos(gastos_ejemplo, "Gastos Pre-cargados")
    
    while True:
        mostrar_menu()
        opcion = obtener_opcion_valida()
        
        if opcion == 1:
            agregar_gasto(gastos_ejemplo)
        elif opcion == 2:
            mostrar_gastos(gastos_ejemplo, "Todos los Gastos")
        elif opcion == 3:
            resumen_categorias(gastos_ejemplo)
        elif opcion == 4:
            reporte_mensual(gastos_ejemplo)
        elif opcion == 5:
            print("\n¡Hasta luego! 🌟")
            break

if __name__ == "__main__":
    main()
