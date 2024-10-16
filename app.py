{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPil2+CwXxhZkJeR1/8MX+W",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sunbal0123/graphical-calculator/blob/main/calculator.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import sympy as sp\n",
        "import streamlit as st\n",
        "\n",
        "# Title for the app\n",
        "st.title(\"Scientific Graphical Calculator\")\n",
        "\n",
        "# Define a function for basic arithmetic operations\n",
        "def basic_operations():\n",
        "    st.subheader(\"Basic Operations\")\n",
        "    operation = st.selectbox(\"Choose an operation:\", ['+', '-', '*', '/'])\n",
        "    num1 = st.number_input(\"Enter first number:\", value=0.0)\n",
        "    num2 = st.number_input(\"Enter second number:\", value=0.0)\n",
        "\n",
        "    if st.button(\"Calculate\"):\n",
        "        if operation == '+':\n",
        "            result = num1 + num2\n",
        "        elif operation == '-':\n",
        "            result = num1 - num2\n",
        "        elif operation == '*':\n",
        "            result = num1 * num2\n",
        "        elif operation == '/':\n",
        "            if num2 != 0:\n",
        "                result = num1 / num2\n",
        "            else:\n",
        "                st.error(\"Error! Division by zero.\")\n",
        "                return\n",
        "        st.write(f\"Result: {result}\")\n",
        "\n",
        "# Define a function for scientific operations using SymPy\n",
        "def scientific_operations():\n",
        "    st.subheader(\"Scientific Operations\")\n",
        "    operation = st.selectbox(\"Choose an operation:\", ['Solve Equations', 'Derivative', 'Integral'])\n",
        "    x = sp.Symbol('x')\n",
        "    equation = st.text_input(\"Enter an expression in terms of 'x' (e.g., x**2 + 3*x + 2):\")\n",
        "\n",
        "    if st.button(\"Calculate\"):\n",
        "        try:\n",
        "            if operation == 'Solve Equations':\n",
        "                solution = sp.solve(sp.sympify(equation), x)\n",
        "                st.write(f\"Solutions: {solution}\")\n",
        "            elif operation == 'Derivative':\n",
        "                derivative = sp.diff(sp.sympify(equation), x)\n",
        "                st.write(f\"Derivative: {derivative}\")\n",
        "            elif operation == 'Integral':\n",
        "                integral = sp.integrate(sp.sympify(equation), x)\n",
        "                st.write(f\"Integral: {integral}\")\n",
        "        except Exception as e:\n",
        "            st.error(f\"Error in computation: {e}\")\n",
        "\n",
        "# Define a function for graphing using Matplotlib and NumPy\n",
        "def graph_function():\n",
        "    st.subheader(\"Graphing\")\n",
        "    func = st.text_input(\"Enter a function to graph in terms of 'x' (e.g., np.sin(x), x**2):\")\n",
        "\n",
        "    if st.button(\"Plot Graph\"):\n",
        "        try:\n",
        "            x = np.linspace(-10, 10, 400)  # Generate values from -10 to 10\n",
        "            y = eval(func)\n",
        "            fig, ax = plt.subplots()\n",
        "            ax.plot(x, y)\n",
        "            ax.set_title(f\"Graph of {func}\")\n",
        "            ax.set_xlabel('x')\n",
        "            ax.set_ylabel('y')\n",
        "            ax.grid(True)\n",
        "            st.pyplot(fig)\n",
        "        except Exception as e:\n",
        "            st.error(f\"Error plotting graph: {e}\")\n",
        "\n",
        "# Main function to control the app\n",
        "def main():\n",
        "    st.sidebar.title(\"Calculator Menu\")\n",
        "    option = st.sidebar.selectbox(\"Choose an option:\", [\"Basic Operations\", \"Scientific Operations\", \"Graph Function\"])\n",
        "\n",
        "    if option == \"Basic Operations\":\n",
        "        basic_operations()\n",
        "    elif option == \"Scientific Operations\":\n",
        "        scientific_operations()\n",
        "    elif option == \"Graph Function\":\n",
        "        graph_function()\n",
        "\n",
        "# Run the app\n",
        "if __name__ == \"__main__\":\n",
        "    main()\n"
      ],
      "metadata": {
        "id": "NoF0L_aF0Hpr"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
