import xlsxwriter
from unittest import result

#   새파일생성
workbook = xlsxwriter.Workbook('bulk_test.xlsx')
worksheet = workbook.add_worksheet()

###   제목  ###
#   상품기본정보
worksheet.merge_range('A1:E1','상품기본정보',)
worksheet.write('A2', '노출카테고리')
worksheet.write('B2', '상품명')
worksheet.write('C2', '판매요청시작일')
worksheet.write('D2', '판매요청종료일')
worksheet.write('E2', '브랜드')

#   Item 속성 정보
worksheet.merge_range('F1:M1','Item 속성 정보',)
worksheet.write('F2', '속성타입1')
worksheet.write('G2', '속성값1')
worksheet.write('H2', '속성타입2')
worksheet.write('I2', '속성값2')
worksheet.write('J2', '속성타입3')
worksheet.write('K2', '속성값3')
worksheet.write('L2', '속성타입4')
worksheet.write('M2', '속성값4')

# Item  구성 정보
worksheet.merge_range('N1:AB1','Item  구성 정보',)
worksheet.write('N2', '판매가격')
worksheet.write('O2', '판매대행수수료')
worksheet.write('P2', '할인율기준가')
worksheet.write('Q2', '판매가능수량')
worksheet.write('R2', '기준출고일')
worksheet.write('S2', '단위수량')
worksheet.write('T2', '인당최대구매수량')
worksheet.write('U2', '최대구매수량기간(일)')
worksheet.write('V2', '19세이상')
worksheet.write('W2', '과세여부')
worksheet.write('X2', '병행수입여부')
worksheet.write('Y2', '해외구매대행')
worksheet.write('Z2', '업체상품코드')
worksheet.write('AA2', '바코드')
worksheet.write('AB2', '모델번호')

#   상품고시정보
worksheet.merge_range('AC1:AQ1','상품고시정보',)
worksheet.write('AC2', '상품고시정보 카테고리')
worksheet.write('AD2', '상품고시정보값1')
worksheet.write('AE2', '상품고시정보값2')
worksheet.write('AF2', '상품고시정보값3')
worksheet.write('AG2', '상품고시정보값4')
worksheet.write('AH2', '상품고시정보값5')
worksheet.write('AI2', '상품고시정보값6')
worksheet.write('AJ2', '상품고시정보값7')
worksheet.write('AK2', '상품고시정보값8')
worksheet.write('AL2', '상품고시정보값9')
worksheet.write('AM2', '상품고시정보값10')
worksheet.write('AN2', '상품고시정보값11')
worksheet.write('AO2', '상품고시정보값12')
worksheet.write('AP2', '상품고시정보값13')
worksheet.write('AQ2', '상품고시정보값14')

#   이미지
worksheet.merge_range('AR1:AT1','이미지',)
worksheet.write('AR2', '대표이미지(정사각형)')
worksheet.write('AS2', '대표이미지(직사각형)')
worksheet.write('AT2', '기타이미지')

#   상품 상세 설명
worksheet.write('AU1','상품 상세 설명',)
worksheet.write('AU2', '상세 설명')

#   구비서류
worksheet.merge_range('AV1:BB1','구비서류',)
worksheet.write('AV2', '구비서류값1')
worksheet.write('AW2', '구비서류값2')
worksheet.write('AX2', '구비서류값3')
worksheet.write('AY2', '구비서류값4')
worksheet.write('AZ2', '구비서류값5')
worksheet.write('BA2', '구비서류값6')
worksheet.write('BB2', '구비서류값7')


