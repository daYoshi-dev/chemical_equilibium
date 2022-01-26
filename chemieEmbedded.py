import tkinter as tk
import tkinter.ttk as ttk
import matplotlib.pyplot as plt
from matplotlib import gridspec
import pandas
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


"""
This class does this calculation part and stores the results in the arrays
"""
class reaction:

    def calculation(self, reactantS, productS, rateS, iterationS):
        curr_rate_arr = []
        product_arr = []
        reactant_arr = []
        reactant = reactantS
        product = productS
        kc = rateS
        reaction_part = 0.01
        iteration = iterationS

        table_matrix = self.calc_all(reactant, product, kc, reaction_part, iteration, curr_rate_arr, product_arr, reactant_arr)
        return reactant_arr, product_arr, curr_rate_arr

    def calculate(self, reactantS, productS, kc, reaction_part):
        reactant = reactantS - round(reactantS / 1 * reaction_part) + round(productS / kc * reaction_part)
        product = productS - round(productS/ kc * reaction_part) + round(reactantS / 1 * reaction_part)
        return reactant, product

    def calc_all(self, reactant, product, kc, reaction_part, iteration, curr_rate_arr, product_arr, reactant_arr):

        for i in range(iteration):
            reactant, product = self.calculate(reactant, product, kc, reaction_part)
            i += 1

            curr_rate_arr.append(product / reactant)
            product_arr.append(product)
            reactant_arr.append(reactant)

        table_matrix = [reactant_arr, product_arr, curr_rate_arr]
        return table_matrix

"""
https://www.geeksforgeeks.org/create-table-using-tkinter/
"""

class table:

     def __init__(self, values, windowS):
         tree = ttk.Treeview(windowS, columns=('Edukt', 'Produkt', 'KC'), show='headings')

         for i in range(0, len(values) -1):
                tree.insert('', 'end', iid=None, values=values[i])
                i += 1

         windowS.add(tree)


class window:

    def createWindow(self):
        display = tk.PanedWindow()
        return display


class graph:

    def __init__(self, iteration, kc, tmatrix, windowS):

        # GER: Erstellen der Koord-Systeme
        # ENG: Definition of coordinate systems
        plt.ion()
        fig = plt.figure()
        gs = gridspec.GridSpec(2, 1, height_ratios=[2, 3])

        # GER: Sys 1: Edukte & Produkte
        # ENG: Sys 1: Educts & Products

        ax0 = plt.subplot(gs[0], title='Edukte und Produkte', xlabel='Zeit', ylabel='Menge')
        ax0.set_xscale('log')

        ax0.grid()

        # GER: Achsen
        # ENG: Axis
        ax0.set_xscale('log')
        ax0.set_yscale('linear')

        ax0.set_xlim([1, iteration])
        ax0.set_ylim([1, tmatrix[0][0] + tmatrix[1][0]])

        # GER: Linien
        # ENG: Graphs

        rline, = ax0.plot(range(0, len(tmatrix[0])), tmatrix[0], 'b', label='Edukte')
        pline, = ax0.plot(range(0, len(tmatrix[0])), tmatrix[1], 'r', label='Produkte')

        # GER: Sys 2: Verhaeltnis und Kc
        # ENG: Sys 2: Ratio and Kc

        ax1 = plt.subplot(gs[1], sharex=ax0, title='Verhältnis und Kc', xlabel='Zeit', ylabel='Stoffverhältnis')
        ax1.grid()

        # GER: Achsen
        # ENG: Axis

        ax1.set_xscale('log')
        ax1.set_yscale('linear')

        ax1.set_xlim([1, iteration])
        ax1.set_ylim([0, kc + 1])

        # GER: Linen
        # ENG: Graphs

        kline = ax1.hlines(kc, 1, iteration, 'black', label='kc')
        vline, = ax1.plot(range(0, len(tmatrix[0])), tmatrix[2], 'g', label='Edukt-Produkt-Verhältnis')

        # GER: Legende
        # ENG: Legend
        ax0.legend(loc='center right')
        ax1.legend(loc='lower right')

        # GER/ENG: Padding
        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=windowS)
        canvas.get_tk_widget().pack()
        toolbar = NavigationToolbar2Tk(canvas, windowS)
        canvas.get_tk_widget().pack()

        windowS.add(canvas)

class app:

    def __init__(self, reactantS, productS, rateS, iterationS):
        display = window().createWindow()
        reaction_results = reaction().calculation(reactantS, productS, rateS, iterationS)
        graph(iterationS, rateS, reaction_results, display)
        table(reaction_results, display)
        print(self.switch_axis_array(reaction_results))

        display.mainloop()

    def switch_axis_array(self, to_switch):

        new_arr = []
        element = []

        for i in range(0, len(to_switch[1])):
            for j in range(0, len(to_switch)):
                element.append(to_switch[j][i])
                j += 1
            new_arr.append(element)
            element = []
            i += 1

        return new_arr

def main():
    print(main)
    app(10000, 0, 3, 200)

if __name__ == "__main__":
    main()










