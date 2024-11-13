import nltk
from nltk.tokenize import word_tokenize    #라이브러리 불러오기
nltk.download('punkt_tab')
import random
from fpdf import FPDF

text = input('영어 지문을 입력한 후 [Enter] : ')       #영어 지문 입력 받기
cloze_num = int(input('생성할 빈칸의 개수 입력 후 [Enter] : '))   #빈칸 개수 입력 받기


def create_cloze(text, cloze_num) :
    word = word_tokenize(text)    #지문 토큰화 (단어별로 나눔, 리스트 형태로 만듦)
    word_num = random.sample(range(len(word)), cloze_num)   # 0 ~ 단어 개수 - 1까지 리스트 생성 후 입력받은 수만큼 무작위로 추출해 저장
    for num in word_num:
        word[num] = '(              )'    #추출한 수들의 인덱스 번호를 가진 단어를 빈칸으로 바꾸기

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, ' '.join(word))    #pdf 생성
    pdf.output("cloze_test.pdf")

create_cloze(text, cloze_num)  #함수 실행