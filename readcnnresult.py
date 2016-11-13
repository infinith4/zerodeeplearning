import pickle

with open('params.pkl','rb') as f2:
    data=pickle.load(f2)	#まずリストで受ける
    print('pickleに入っているデータ：\n',data)
    print('各要素を確認する\n')
    for i in range(len(data)):
        print(i,data[i],type(data[i]))