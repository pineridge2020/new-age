from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class SalesTab(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        items = ['Shawarma', 'Buffalo wings', 'Platter', 'Defleshed chicken']
        self.inputs = {}
        for item in items:
            box = BoxLayout(orientation='horizontal')
            label = Label(text=item)
            input_box = TextInput(input_filter='int', multiline=False)
            self.inputs[item] = input_box
            box.add_widget(label)
            box.add_widget(input_box)
            self.add_widget(box)
        calc_box = BoxLayout(orientation='horizontal')
        self.total_label = Label(text='Total Sales: 0')
        calc_button = Button(text='Calculate')
        calc_button.bind(on_press=self.calculate_total_sales)
        calc_box.add_widget(self.total_label)
        calc_box.add_widget(calc_button)
        self.add_widget(calc_box)

    def calculate_total_sales(self, instance):
        total = sum(int(self.inputs[item].text or 0) for item in self.inputs)
        self.total_label.text = f'Total Sales: {total}'

class OrdersTab(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        items = ['Chicken', 'Chapati', 'Lettuce', 'Potatoes', 'Tomato sauce', 'Mustard Sauce', 'Chilli Sauce', 'Eggs', 'Garlic', 'Cooking oil', 'Salt', 'Wrapping paper', 'Carrier bags', 'Serviettes', 'Tooth picks', 'Forks', 'Gas', 'Out Sourced Wings']
        self.inputs = {}
        for item in items:
            box = BoxLayout(orientation='horizontal')
            label = Label(text=item)
            input_box = TextInput(input_filter='int', multiline=False)
            self.inputs[item] = input_box
            box.add_widget(label)
            box.add_widget(input_box)
            self.add_widget(box)
        calc_box = BoxLayout(orientation='horizontal')
        self.total_label = Label(text='Total Orders: 0')
        calc_button = Button(text='Calculate')
        calc_button.bind(on_press=self.calculate_total_orders)
        calc_box.add_widget(self.total_label)
        calc_box.add_widget(calc_button)
        self.add_widget(calc_box)

    def calculate_total_orders(self, instance):
        total = sum(int(self.inputs[item].text or 0) for item in self.inputs)
        self.total_label.text = f'Total Orders: {total}'

class TransportTab(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text='Transport Amount'))
        self.transport_input = TextInput(input_filter='int', multiline=False)
        self.add_widget(self.transport_input)

class AccountsTab(BoxLayout):
    def __init__(self, sales_tab, orders_tab, transport_tab, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.sales_tab = sales_tab
        self.orders_tab = orders_tab
        self.transport_tab = transport_tab
        self.total_sales_label = Label(text='Total Sales: 0')
        self.total_orders_label = Label(text='Total Orders: 0')
        self.total_expenses_label = Label(text='Total Expenses: 0')
        self.net_gain_label = Label(text='Net Gain: 0')
        self.add_widget(self.total_sales_label)
        self.add_widget(self.total_orders_label)
        self.add_widget(self.total_expenses_label)
        self.add_widget(self.net_gain_label)
        calc_button = Button(text='Calculate')
        calc_button.bind(on_press=self.calculate_totals)
        self.add_widget(calc_button)

    def calculate_totals(self, instance):
        total_sales = sum(int(self.sales_tab.inputs[item].text or 0) for item in self.sales_tab.inputs)
        total_orders = sum(int(self.orders_tab.inputs[item].text or 0) for item in self.orders_tab.inputs)
        total_expenses = int(self.transport_tab.transport_input.text or 0)
        self.total_sales_label.text = f'Total Sales: {total_sales}'
        self.total_orders_label.text = f'Total Orders: {total_orders}'
        self.total_expenses_label.text = f'Total Expenses: {total_expenses}'
        net_gain = total_sales - total_orders - total_expenses
        self.net_gain_label.text = f'Net Gain: {net_gain}'

class ShawarmaTabPanel(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.do_default_tab = False
        self.sales_tab = SalesTab()
        self.orders_tab = OrdersTab()
        self.transport_tab = TransportTab()
        self.add_widget(self.sales_tab)
        self.add_widget(self.orders_tab)
        self.add_widget(self.transport_tab)
        self.add_widget(BoxLayout())
        self.accounts_tab = AccountsTab(self.sales_tab, self.orders_tab, self.transport_tab)
        self.add_widget(self.accounts_tab)

class ShawarmaApp(App):
    def build(self):
        return ShawarmaTabPanel()

if __name__ == '__main__':
    ShawarmaApp().run()
