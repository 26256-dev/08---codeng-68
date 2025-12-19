{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/26256-dev/08---codeng-68/blob/main/mid-08-Bas.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Wf5KrEb6vrkR"
      },
      "source": [
        "# ยินดีต้อนรับสู่ Colab"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"โปรเเกรมเลขคู่หรือเลขคี่\")\n",
        "print () #เว้น\n",
        "Number = input(\"ตัวเลข: \")\n",
        "\n",
        "if Number.isdigit():\n",
        "    num = int(Number)\n",
        "    if num % 2 == 0:\n",
        "        print(f\"{num} เป็นเลขคู่\")\n",
        "    else:\n",
        "        print(f\"{num} เป็นเลขคี่\")\n",
        "else:\n",
        "    print(\"Erorr\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6RgqM0ZPrydR",
        "outputId": "369dbff8-d862-43c3-b99a-7b7b9420c30a"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "โปรเเกรมเลขคู่หรือเลขคี่\n",
            "\n",
            "ตัวเลข: 2.556245\n",
            "Erorr\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "name": "ยินดีต้อนรับสู่ Colab",
      "toc_visible": true,
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}