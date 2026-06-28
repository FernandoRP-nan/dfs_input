# Buscador de Caminos — 8-Puzzle con DFS

Proyecto académico de **inteligencia artificial**: resuelve el puzzle 8 usando **búsqueda en profundidad** con límite de profundidad configurable.

## Requisitos

- Python 3.9+

## Uso rápido

```bash
python main.py \
  --initial "1,2,3,4,5,6,7,0,8" \
  --final "1,2,3,4,5,6,7,8,0" \
  --depth 25
```

### Parámetros

| Flag | Descripción |
|------|-------------|
| `--initial` | 9 números (0-8), separados por coma. `0` = casilla vacía |
| `--final` | Estado objetivo, mismo formato |
| `--depth` | Profundidad máxima (default: 20) |
| `--verbose` | Imprime cada tablero intermedio |

## Ejemplo de salida

```
Estado inicial:
1 2 3
4 5 6
7 0 8

Estado objetivo:
1 2 3
4 5 6
7 8 0

Nodos explorados: 3

✅ Solución encontrada en 1 movimientos:
 derecha
```

## Estructura

```
main.py           # CLI (argparse)
puzzle_solver.py  # Validación, movimientos y DFS
DFS.py            # Versión original interactiva (legacy)
```

## Modo interactivo (legacy)

```bash
python DFS.py
```

## Validaciones

- Tablero de 9 celdas con dígitos únicos 0-8
- Mensaje claro si no hay solución dentro del límite de profundidad
- DFS con pila LIFO (orden correcto de profundidad)

## Autor

Fernando Rodríguez Prianti — ITS Xalapa
