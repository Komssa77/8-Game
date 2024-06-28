import PySimpleGUI as sg

def main():
    table_width = 600
    table_height = 300
    ball_radius = 10
    pocket_radius = 15

    whiteBallPos = (table_width//4,table_height//2)
    BlackBallPos = ((3*table_width)//4,table_height//2)

    layout = [
        [sg.Graph((table_width, table_height), (0, table_height), (table_width, 0), key='canvas')],
        [sg.Button('Exit')]
    ]

    window = sg.Window('Pool Table', layout, resizable=True, finalize=True)
    window.bind('<Motion>', 'Motion')
    window.bind("<Button-1>", 'Window Click')

    # Function to draw the pool table
    def draw_pool_table(whiteBallPos, BlackBallPos):
        canvas = window['canvas']
        canvas.erase()
        
        #border
        canvas.draw_rectangle((0, 0), (table_width, table_height), line_color='brown', line_width=3)
        
        #pockets
        pocket_positions = [(0, 0), (table_width // 2, 0), (table_width, 0),
                            (0, table_height), (table_width // 2, table_height), (table_width, table_height)]
        for pos in pocket_positions:
            canvas.draw_circle(pos, pocket_radius, fill_color='black')

        #for pos in whiteBallPos: 
        canvas.draw_circle(whiteBallPos, ball_radius, fill_color='white', line_color='black')
        canvas.draw_circle(BlackBallPos, ball_radius, fill_color='black', line_color='white')
        canvas.draw_circle((10,10), ball_radius, fill_color='black', line_color='white')

    # Initial drawing of the pool table
    draw_pool_table(whiteBallPos,BlackBallPos)


    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        # if user closes window or clicks cancel
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        elif event == 'Motion':
            e = window.user_bind_event
            print(f'X: {e.x}')
            print(f'Y: {e.y}')
        elif event == 'Window Click':
            e = window.user_bind_event
            print('CLICK')
            draw_pool_table((e.x,e.y),BlackBallPos) 
            print(e)
           
    window.close()

if __name__ == '__main__':
    main()


