# Importar la libreri pip install nicegui
from nicegui import ui
import pandas as pd


# Link de referencia https://docs.python.org/es/3/tutorial/datastructures.html#

# Definir Lista
item = [20, 50, 9, 45, 9, 78, 56, 3]

# Definit los metodos para la lista
def render_list():     #el def es definir una funcion y render_list es el nombre de la funcion 
    # Dibujar los cuadros de memoria de mi lista
    list_container.clear()
    with list_container:
        if not item:
            ui.label('Lista vacía').classes('text-gray-400 italic')
            return

        with ui.row().classes('items-center gap-2 flex-wrap'):
            for idx, val in enumerate(item):
                with ui.column().classes('items-center gap-1'):
                    # Muestra el valor de elemento
                    ui.label(str(val)).classes('w-16 h-16 flex items-center justify-center '
                        'bg-blue-800 text-white font-bold text-lg rounded-lg shadow-md')
                    # Muestra el indice del elemento
                    ui.label(f'[{idx}]*').classes('text-xs font-semibold text-slate-700')

# Metodo append
def do_append():
    if val_input.value is not None:
        item.append(val_input.value)
        render_list() 
    else:
        ui.notify('Error: Debes introducir un valor para usar append().', color='warning')   

# Metodo Insert
def do_insert():
    if val_input.value is not None and idx_input is not None:
        idx = max(0, min(int(idx_input.value), len(item)))
        item.insert(idx, val_input.value)
        render_list()
    else:
        ui.notify('Error: Faltan datos (Valor o Índice) para realizar insert().', color='warning')

# Metodo Pop
def do_pop():
    if not item:
        ui.notify('Error: La lista está vacía, no se puede hacer pop().', color='negative')
        return
    
    if idx_input is not None:
            idx = max(0, min(int(idx_input.value), len(item)))
            item.pop(idx-1)
            render_list()

# Metodo Clear
def do_clear():
    item.clear()
    render_list()

#metodo extend 
def do_extend():
    if val_input.value is not None:
        # Permite agregar multiples numeros separados por comas
        raw = str(val_input.value).split(',')
        try:
            valores = [int(v.strip()) for v in raw if v.strip() != '']
            if valores:
                item.extend(valores)
                render_list()
            else:
                ui.notify('Error: No ingresaste numeros validos.', color='warning')
        except ValueError:
            ui.notify('Error: Ingrese solo numeros separados por coma.', color='negative')
    else:
        ui.notify('Error: Ingresa valores en "Valor" para usar extend().', color='warning')

#Metodo Remove
def do_remove():
    try:
        item.remove(int(val_input.value))
        render_list()
    except (ValueError, TypeError):
        ui.notify('Error: Ingresa un numero válido que esté en la lista.', color='warning')

#Metodo Index
def do_index():
    try:
        idx = item.index(int(val_input.value))
        ui.notify(f'El índice del valor {val_input.value} es: {idx}', color='info')
    except ValueError:
        ui.notify('Error: El valor no se encuentra en la lista.', color='warning')

#METODO COUNT 
def do_count():
    try:
        count = item.count(int(val_input.value))
        ui.notify(f'El valor {val_input.value} aparece {count} veces en la lista.', color='info')
    except ValueError:
        ui.notify('Error: Ingresa un numero valido para contar.', color='warning')

#METODO SORT
def do_sort():
    item.sort()
    render_list()
    ui.notify('La lista ha sido ordenada de menor a mayor.', color='info')

#METODO REVERSE  
def do_reverse():
    item.reverse()
    render_list()
    ui.notify('La lista ha sido invertida.', color='info')  #ui es la interfaz de usuario y notify es para mostrar un mensaje en la pantalla

#METODO COPY
def do_copy():  #do copy es el nombre de la funcion y sirve para hacer una copia de la lista
    item_copy = item.copy()
    ui.notify(f'Se ha creado una copia de la lista: {item_copy}', color='info')


# Interface
ui.page_title('Visualizador de Listas en Python con NiceGui')   #page_title es para poner un titulo en la pagina y el texto es el titulo que se va a mostrar

# Contenedor Principal
with ui.column().classes('p-6 gap-6 w-full'):  #with es para crear un contenedor y column es para poner los elementos en columna y classes es para poner clases de css y p-6 es para poner un padding de 6 y gap-6 es para poner un espacio entre los elementos de 6 y w-full es para poner el ancho completo
    ui.label('Practica Grafica de una Lista').classes('text-2xl font-bold text-state-800')

    # Contenedor de los espacios de memoria
    with ui.card().classes('w-full p-4 min-h-[140px] bg-slate-50 border-slate-200'):
        list_container = ui.row().classes('w-full items-center')

    # Panel de Control (Las entradas y los Metodos)
    with ui.card().classes('w-full p-4 gap-4'):
        ui.label('OPERACIONES').classes('text-sm font-semibold text-slate-500')   

        # Contenedor de entrada de datos
        with ui.row().classes('gap-4 items-center'):  #ui.row es para poner los elementos en fila y cla.sses es para poner clases de css y gap-4 es para poner un espacio entre los elementos de 4 y items-center es para centrar los elementos verticalmente
            val_input = ui.number('Valor', placeholder="Introduce un número").classes('w-40') #val_input es el nombre de la variable y ui.number es para crear un input de tipo numero y placeholder es para poner un texto dentro del input y classes es para poner clases de css y w-40 es para poner un ancho de 40 
            idx_input = ui.number('Indice', value=0, min=0).classes('w-40')   #idx es indice     input es el nombre de la variable

        # Contenedor de botones de accion
        with ui.row(): # ui.row es para poner los elementos en la fila 
            ui.button('append(x)', icon='add', color='secondary', on_click=do_append)    #ui.button es para crear un boton
            ui.button('insert(i)', icon='add_circle', color='info', on_click=do_insert)
            ui.button('pop(i)', icon='remove', color='warning', on_click=do_pop)
            ui.button('clear()', icon='delete', color='red', on_click=do_clear)
            ui.button('extend([x])', icon='add_link', color='info', on_click=do_extend)
            ui.button('remove(x)', icon='remove_circle', color='orange', on_click=do_remove)
            ui.button('index(x)', icon='search', color='primary', on_click=do_index)
            ui.button('count(x)', icon='format_list_numbered', color='secondary', on_click=do_count)
            ui.button('sort()', icon='sort', color='blue', on_click=do_sort)
            ui.button('reverse()', icon='swap_vert', color='purple', on_click=do_reverse)
            ui.button('copy()', icon='content_copy', color='teal', on_click=do_copy)
render_list()
ui.run()