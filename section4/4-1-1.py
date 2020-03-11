import pickle

#파일 이름 데이터
bfilename = 'D:/atom_py/section4/test.bin'
tfilename = 'D:/atom_py/section4/test.txt'

data1=677
data2="Hello World"
data3=['car', 'animal', 'house']

# 바이너리 쓰기(객체의 직렬화) -----------------서로 암호 복호
with open(bfilename, "wb") as f:
    pickle.dump(data1,f) #dumps(문자열)=>loads가 짝꿍 / dump(문자)=> load가 짝꿍
    pickle.dump(data2,f)
    pickle.dump(data3,f)

    # pickle.dumps(data1,data2,data3,f)
    # 아  data1,data2,data3를 나열한다는게 아니라, 한파일에 문자열을 쓴다는 얘기인듯

#텍스트 쓰기
with open(tfilename, "wt") as f:
    f.write(str(data1))
    f.write('\n')
    f.write(data2)
    f.write('\n')
    f.writelines('\n'.join(data3))
    f.write('\n')

# 바이너리로 읽기(역직렬화) -----------------서로 암호 복호
with open(bfilename, "rb") as f:
    b=pickle.load(f)
    print(type(b),'Binary Read |',b)
    b=pickle.load(f)
    print(type(b),'Binary Read |',b)
    b=pickle.load(f)
    print(type(b),'Binary Read |',b)
    print()

    # c=pickle.loads(f) #위에가 덤프즈 여야 되는 듯.
    # print(c)

#텍스트 읽기
with open(tfilename, "rt") as f:
    for i,line in enumerate(f,1):
        print(type(line), 'Text Read'+str(i)+'|', line, end='')















#
