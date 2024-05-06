import flet as ft
import random

def main(page : ft.Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'

    categories_card = ft.Row(
        scroll = 'auto'
        
    )

    categories = ['Family', 'Business', 'Friends', 'Work', 'vacation']
    for index, category in enumerate(categories):
        categories_card.controls.append(
            ft.Container(
                bgcolor = BG, 
                height = 110, 
                width = 170,
                padding = 15,
                border_radius = 20,
                content = ft.Column(
                    controls = [
                        ft.Text('40 tasks'),
                        ft.Text(category),
                        ft.Container(
                            width = 160,
                            height = 5,
                            bgcolor ='white12',
                            border_radius = 20,
                            padding = ft.padding.only(right = ((1 + index) * 20)),
                            content = ft.Container(bgcolor = PINK, )
                        )
                    ]
                )

            )
        )

    tasks = (

    )

    first_page_contents = ft.Container(
        content = ft.Column(
            controls = [
                ft.Row(
                    alignment = 'spaceBetween',
                    controls = [
                        ft.Container(
                            content = ft.Icon(
                                ft.icons.MENU
                            ) 
                        ), 
                        ft.Row(
                            controls = [
                                ft.Icon(ft.icons.SEARCH),
                                ft.Icon(ft.icons.NOTIFICATIONS)
                            ]
                        )
                    ]
                ),
                ft.Text(value = 'Welcome Back, Flavian'),
                ft.Text(value = 'CATEGORIES'),
                ft.Container(
                    padding = ft.padding.only(top = 10, bottom = 20),
                    content = categories_card
                )
            ]
        )
    )

    page1 = ft.Container()

    page2 = ft.Row(
        controls = [
            ft.Container(
                width = 300,
                height = 650,
                bgcolor = FG,
                border_radius = 20,
                padding = ft.padding.only(
                    top = 20, left = 10, right = 20, bottom = 5,
                ),
                content = ft.Column(
                    controls = [
                        first_page_contents,
                    ]
                )
            ),
            ft.Container(height=20),
            ft.Text(value = "TODAY'S TASKS"),
            ft.Stack(
                controls = [
                    # tasks,
                    ft.FloatingActionButton(),
                ]
            )
        ]
    )

    container = ft.Container(
        width = 300,
        height = 650,
        bgcolor = BG,
        border_radius = 20,
        content = ft.Stack(
            controls = [
                page1,
                page2,
            ]
        ) 
    )

    page.add(container)


ft.app(target = main)