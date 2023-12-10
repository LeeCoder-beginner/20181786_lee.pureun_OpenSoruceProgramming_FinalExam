{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyORYeC9DRZt1ggg2rKjbHUy",
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
        "<a href=\"https://colab.research.google.com/github/LeeCoder-beginner/20181786_lee.pureun_OpenSoruceProgramming_FinalExam/blob/main/Open_source_Programming_Final_Exam.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "i5gmOJM50aBB"
      },
      "outputs": [],
      "source": [
        "#<오픈소스프로그래밍 기말 프로젝트>\n",
        "#\n",
        "# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.\n",
        "# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.\n",
        "#\n",
        "# 학번 : ________ 이름 : ______\n",
        "\n",
        "import os\n",
        "import time\n",
        "\n",
        "# Q.1 10점\n",
        "#\n",
        "# 문자열 my_string과 target이 매개변수로 주어질 때,\n",
        "# target이 문자열 my_string의 부분 문자열이라면 1을,\n",
        "# 아니라면 0을 return 하는 solution 함수를 작성하시오.\n",
        "#\n",
        "# 제한사항\n",
        "# 1 ≤ my_string 의 길이 ≤ 100\n",
        "# my_string 은 영소문자로만 이루어져 있습니다.\n",
        "# 1 ≤ target 의 길이 ≤ 100\n",
        "# target 은 영소문자로만 이루어져 있습니다.\n",
        "\n",
        "def solution(my_strung, target):\n",
        "    answer = 0\n",
        "    return answer\n",
        "\n",
        "# Q.2 10점\n",
        "#\n",
        "# 모스부호 해독 프로그램 만들기\n",
        "# 문자열 letter 가 매개변수로 주어질 때,\n",
        "# letter 영어 소문자로 바꾼 문자열을 return 하는\n",
        "# solution 함수를 완성하시오.\n",
        "#\n",
        "# 제한사항\n",
        "# 1 ≤ letter 의 길이 ≤ 1,000\n",
        "# letter 의 모스부호는 공백으로 나누어져 있습니다.\n",
        "# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.\n",
        "#\n",
        "# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.\n",
        "\n",
        "def solution(letter):\n",
        "    morse = {\n",
        "    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',\n",
        "    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',\n",
        "    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',\n",
        "    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',\n",
        "    '-.--':'y','--..':'z'}\n",
        "    answer = ''\n",
        "    return answer\n",
        "\n",
        "# Q.3 10점\n",
        "#\n",
        "# 행성의 나이를 알파벳으로 표현할 때,\n",
        "# a는 0, b는 1, ..., j는 9\n",
        "# 예를 들어 cd는 23살, fb는 51살입니다.\n",
        "# age가 매개변수로 주어질 때\n",
        "# PROGEAMMER-857식 나이를 return 하도록\n",
        "# solution 함수를 완성하시오.\n",
        "#\n",
        "# 제한사항\n",
        "# age는 자연수입니다.\n",
        "# age ≤ 1,000\n",
        "# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.\n",
        "\n",
        "def solution(age):\n",
        "    answer = ''\n",
        "    return answer\n",
        "\n",
        "# Q.4 10점\n",
        "#\n",
        "# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인\n",
        "# 서로 다른 크기의 원이 두 개 주어집니다.\n",
        "# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,\n",
        "# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를\n",
        "# return하도록 solution 함수를 완성해주세요.\n",
        "# ※ 각 원 위의 점도 포함하여 셉니다.\n",
        "#\n",
        "# 제한사항\n",
        "# 1 ≤ r1 < r2 ≤ 1,000,000\n",
        "\n",
        "def solution(r1, r2):\n",
        "    answer = 0\n",
        "    return answer\n",
        "\n",
        "# Q.5 10점\n",
        "#\n",
        "# 0 또는 양의 정수가 주어졌을 때,\n",
        "# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.\n",
        "#\n",
        "# 예를 들어, 주어진 정수가 [6, 10, 2]라면\n",
        "# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,\n",
        "# 이중 가장 큰 수는 6210입니다.\n",
        "#\n",
        "# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,\n",
        "# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어\n",
        "# return 하도록 solution 함수를 작성해주세요.\n",
        "#\n",
        "# 제한사항\n",
        "# numbers의 길이는 1 이상 100,000 이하입니다.\n",
        "# numbers의 원소는 0 이상 1,000 이하입니다.\n",
        "# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.\n",
        "#\n",
        "# numbers = [8, 30, 17, 2, 23]\n",
        "\n",
        "def solution(numbers):\n",
        "    answer = ''\n",
        "    return answer"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Q.1 10점\n",
        "#\n",
        "# 문자열 my_string과 target이 매개변수로 주어질 때,\n",
        "# target이 문자열 my_string의 부분 문자열이라면 1을,\n",
        "# 아니라면 0을 return 하는 solution 함수를 작성하시오.\n",
        "#\n",
        "# 제한사항\n",
        "# 1 ≤ my_string 의 길이 ≤ 100\n",
        "# my_string 은 영소문자로만 이루어져 있습니다.\n",
        "# 1 ≤ target 의 길이 ≤ 100\n",
        "# target 은 영소문자로만 이루어져 있습니다.\n",
        "\n",
        "\n",
        "## target과 my_string을 in 연산자를 통해 비교\n",
        "## 두 개의 매개변수는 영소문자로만 이루어져 있기 때문에 숫자가 있다면 다시 입력하고, 영어 대문자가 포함되어있다면 lower 함수를 통해 영소문자로 바꾼다.\n",
        "\n",
        "\n",
        "\n",
        "def solution(my_string, target):\n",
        "  if target.lower() in my_string.lower():\n",
        "    answer = 1\n",
        "  else:\n",
        "    answer = 0\n",
        "  return answer\n",
        "\n",
        "result = solution(\"Hello World\", \"Hel\")\n",
        "print(result)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "i5OpgmKJDvxs",
        "outputId": "28064cb3-7736-4410-8768-a9134b0b76ec"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# target과 my_string을 입력받는 함수 형성\n",
        "\n",
        "# def a1(my_string, target):\n",
        "#   my_string = input()\n",
        "#   target = input()\n",
        "\n",
        "#   if type(my_string) == int or  type(target) == int:\n",
        "#     a1\n",
        "#   else:\n",
        "#     return my_string, target\n",
        "\n",
        "def solution(my_string, target):\n",
        "  if target.lower() in my_string.lower(): ## if문과 in을 통해 특정 문자열 파악 / lower 함수로 영소문자로 해석\n",
        "    answer = 1\n",
        "  else:\n",
        "    answer = 0\n",
        "  return answer\n",
        "\n",
        "result = solution(input(), input())\n",
        "print(result)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 530
        },
        "id": "sLi6InZ6llqB",
        "outputId": "c09555c2-6243-4bbf-f476-5ee41c703983"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-14-e4893f5368e4>\u001b[0m in \u001b[0;36m<cell line: 19>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     17\u001b[0m   \u001b[0;32mreturn\u001b[0m \u001b[0manswer\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     18\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 19\u001b[0;31m \u001b[0mresult\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0msolution\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     20\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresult\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[0;34m(self, prompt)\u001b[0m\n\u001b[1;32m    849\u001b[0m                 \u001b[0;34m\"raw_input was called, but this frontend does not support input requests.\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    850\u001b[0m             )\n\u001b[0;32m--> 851\u001b[0;31m         return self._input_request(str(prompt),\n\u001b[0m\u001b[1;32m    852\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    853\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_header\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[0;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[1;32m    893\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    894\u001b[0m                 \u001b[0;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 895\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Interrupted by user\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    896\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    897\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Invalid Message:\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Q.2 10점\n",
        "#\n",
        "# 모스부호 해독 프로그램 만들기\n",
        "# 문자열 letter 가 매개변수로 주어질 때,\n",
        "# letter 영어 소문자로 바꾼 문자열을 return 하는\n",
        "# solution 함수를 완성하시오.\n",
        "#\n",
        "# 제한사항\n",
        "# 1 ≤ letter 의 길이 ≤ 1,000\n",
        "# letter 의 모스부호는 공백으로 나누어져 있습니다.\n",
        "# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.\n",
        "#\n",
        "# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.\n",
        "\n",
        "\n",
        "## 미안해라는 말보다 \"고마워, 힘내, 사랑해\"\n",
        "## (My three favourites are) \"Thank you\", \"You did your best\", and \"I love you\".\n",
        "\n",
        "def solution(letter):\n",
        "    morse = {\n",
        "    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',\n",
        "    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',\n",
        "    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',\n",
        "    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',\n",
        "    '-.--':'y','--..':'z'}\n",
        "\n",
        "    a = letter.split() ## 모스부호로 이루어진 코드를 공백으로 split 함수 사용\n",
        "\n",
        "    b = []\n",
        "    answer = ''\n",
        "\n",
        "    for i in range(0, len(a)):\n",
        "      b.append(morse[a[i]])\n",
        "      answer+= str(b[i])\n",
        "\n",
        "\n",
        "    return answer\n",
        "\n",
        "\n",
        "# def morse1(letter):\n",
        "#       morse = {\n",
        "#     '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',\n",
        "#     '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',\n",
        "#     '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',\n",
        "#     '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',\n",
        "#     '-.--':'y','--..':'z'}\n",
        "\n",
        "\n",
        "\n",
        "result = solution('- .... .- -. -.- -.-- --- ..- -.-- --- ..- -.. .. -.. -.-- --- ..- .-. -... . ... - .- -. -.. .. .-.. --- ...- . -.-- --- ..-')\n",
        "print(result)"
      ],
      "metadata": {
        "id": "DYh3Eit-kYMQ",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "7f67bd72-1066-46c5-c46a-58401c0e880a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "thankyouyoudidyourbestandiloveyou\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Q.3 10점\n",
        "#\n",
        "# 행성의 나이를 알파벳으로 표현할 때,\n",
        "# a는 0, b는 1, ..., j는 9\n",
        "# 예를 들어 cd는 23살, fb는 51살입니다.\n",
        "# age가 매개변수로 주어질 때\n",
        "# PROGEAMMER-857식 나이를 return 하도록\n",
        "# solution 함수를 완성하시오.\n",
        "#\n",
        "# 제한사항\n",
        "# age는 자연수입니다.\n",
        "# age ≤ 1,000\n",
        "# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.\n",
        "\n",
        "def solution(age):\n",
        "\n",
        "\n",
        "    answer = ''\n",
        "    for i in range(0, len(age)):\n",
        "      answer += chr(int(age[i]) + 97)\n",
        "\n",
        "\n",
        "    return answer\n",
        "\n",
        "result = solution('857')\n",
        "print('PROGRAMMERS'.lower() + result)"
      ],
      "metadata": {
        "id": "cuz8z5OYprWH",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "aea25f4c-6c0e-4bed-c8c7-61069059784a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "programmersifh\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Q.4 10점\n",
        "#\n",
        "# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인\n",
        "# 서로 다른 크기의 원이 두 개 주어집니다.\n",
        "# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,\n",
        "# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를\n",
        "# return하도록 solution 함수를 완성해주세요.\n",
        "# ※ 각 원 위의 점도 포함하여 셉니다.\n",
        "#\n",
        "# 제한사항\n",
        "# 1 ≤ r1 < r2 ≤ 1,000,000\n",
        "\n",
        "def solution(r1, r2):\n",
        "    answer = 0\n",
        "\n",
        "    answer = (r2 - r1 + 1) * 2\n",
        "\n",
        "    return answer\n",
        "\n",
        "result = solution(10, 20)\n",
        "print(result)"
      ],
      "metadata": {
        "id": "EykBmpmuyfgK",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "37f82d6a-6f85-43f6-f4bf-ea5a5b9286d1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "22\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Q.5 10점\n",
        "#\n",
        "# 0 또는 양의 정수가 주어졌을 때,\n",
        "# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.\n",
        "#\n",
        "# 예를 들어, 주어진 정수가 [6, 10, 2]라면\n",
        "# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,\n",
        "# 이중 가장 큰 수는 6210입니다.\n",
        "#\n",
        "# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,\n",
        "# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어\n",
        "# return 하도록 solution 함수를 작성해주세요.\n",
        "#\n",
        "# 제한사항\n",
        "# numbers의 길이는 1 이상 100,000 이하입니다.\n",
        "# numbers의 원소는 0 이상 1,000 이하입니다.\n",
        "# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.\n",
        "#\n",
        "# numbers = [8, 30, 17, 2, 23]\n",
        "\n",
        "def solution(numbers):\n",
        "    answer = ''\n",
        "    num_str = []\n",
        "\n",
        "\n",
        "    for i in range(0, len(numbers)):\n",
        "      num_str.append(str(numbers[i]))  #numbers의 값을 문자열로 변환\n",
        "\n",
        "    a1 = num_str[0] + num_str[1] + num_str[2]\n",
        "    a2 = num_str[0] + num_str[2] + num_str[1]\n",
        "    a3 = num_str[1] + num_str[0] + num_str[2]\n",
        "    a4 = num_str[1] + num_str[2] + num_str[0]\n",
        "    a5 = num_str[2] + num_str[1] + num_str[0]\n",
        "    a6 = num_str[2] + num_str[0] + num_str[1]\n",
        "\n",
        "    num_int = 0\n",
        "    for i in [a1, a2, a3, a4, a5, a6]:\n",
        "\n",
        "      if num_int > int(i):\n",
        "        continue\n",
        "      else:\n",
        "        num_int = int(i)\n",
        "\n",
        "    answer = str(num_int)\n",
        "    return answer\n",
        "\n",
        "result = solution([5, 6, 11])\n",
        "print(result)"
      ],
      "metadata": {
        "id": "Ff8lLbo7yg-e",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e5cc95c5-0d8c-491a-d74c-5e813bddb88d"
      },
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "6511\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = '11'\n",
        "\n",
        "print(a.split())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 221
        },
        "id": "cmZme5ZIDugz",
        "outputId": "8430c5fa-a514-45f1-8b4c-31182559d27a"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ValueError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-32-60917c9d0ee6>\u001b[0m in \u001b[0;36m<cell line: 3>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0ma\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'11'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ma\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m''\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mValueError\u001b[0m: empty separator"
          ]
        }
      ]
    }
  ]
}