#4.Polinom Kuralı: f(N), k dereceli polinom ise f(N) için Big-O; O(N) olur.
#3.Looplar Kuralı: Bir döngünün çalışma zamanı döngü sayısının bir c sabitiyle çarpımı kadardır.Eğer n değer verilmişse Big-O; O(1) olur.

#Polinomları yazdırmak amacıyla yazılan fonksiyonlar.   #Big(O)-O(N)
def printPoly(poly, n): 
	for i in range(n):  
		print(poly[i], end = "")             #Zamansal Karmaşıklık:c2 + (c0 + c1)*n
		print("x^", exp_1[i], end = "") 
		if (i != n - 1):     
			print(" + ", end = "")   

def printPoly1(poly, n):               
	for i in range(n):            
		print(poly[i], end = "")             #Zamansal Karmaşıklık:c2 + (c0 + c1)*n
		print("x^", exp_2[i], end = "") 
		if (i != n - 1):      
			print(" + ", end = "")
  
#Polinomların toplama işlemi için gerekli fonksiyon.           
def add_coefficient(exp1, coeff1, exp2, coeff2):
    #Oluşturulan listede her indeks bir değer içerir ve bir listede aynı indeks'ten birden fazla olamaz.
    exponent_coefficient_dict = dict()
    #İlk liste çiftini tekrarlayarak ve exp: katsayı çiftleri olarak kaydederiz. 
    for index, exponent in enumerate(exp1):    #Big(O)-O(1)     T(n)=c*n
        exponent_coefficient_dict[exponent] = coeff1[index]
    #Çiftleri depolayarak veya güncelleyerek, ikinci liste çiftini tekrarladık.
    for index, exponent in enumerate(exp2):    #Big(O)-O(1)     T(n)=c*n
        exponent_coefficient_dict[exponent] = exponent_coefficient_dict.get(exponent, 0) + coeff2[index]

    #Oluşan sözlükten anahtarların sıralı bir listesini aldık.
    combined_exp_list = sorted(exponent_coefficient_dict, reverse=True)
    combined_coeff_list = []

    #Sıralamaya göre katsayılar için bir liste oluşturduk.
    #Üslerin görünmesi sağlandı.
    for exponent in combined_exp_list: #Big(O)-O(1)     T(n)=c*n
        combined_coeff_list.append(exponent_coefficient_dict.get(exponent, 0))

    #Polinomların toplamının yazdırılmasını sağlayan işlem.
    for i in range(len(combined_coeff_list)):   #Big(O)-O(N)
      print(combined_coeff_list[i], end = "")   #Zamansal Karmaşıklık:(c2+c3) + (c0 + c1)*n
      print("x^",combined_exp_list[i], end = "")
      if (i != len(combined_coeff_list)-1):
        print(" + ", end = "")

    print("\n", end = "")
    print("\n", end = "") 
    print("[Katsayılar]          [Üsler]")
    return (combined_coeff_list, combined_exp_list)

#Polinomların farkının bulunması için gerekli fonksiyon.
def dif_coefficient(exp1, coeff1, exp2, coeff2):
    exponent_coefficient_dict = dict()
    #İlk liste çiftini tekrarlayıp ve exp: katsayı çiftleri olarak kaydederiz. 
    for index, exponent in enumerate(exp1):  #Big(O)-O(1)   T(n)=c*n
        exponent_coefficient_dict[exponent] = coeff1[index]
    #Çiftleri depolayarak veya güncelleyerek, ikinci liste çiftini tekrarladık.
    for index, exponent in enumerate(exp2):  #Big(O)-O(1)   T(n)=c*n
        exponent_coefficient_dict[exponent] = exponent_coefficient_dict.get(exponent, 0) - coeff2[index]

    #Oluşan sözlükten anahtarların sıralı bir listesini aldık.
    combined_exp_list = sorted(exponent_coefficient_dict, reverse=True)
    combined_coeff_list = []

    #Sıralamaya göre katsayılar için bir liste oluşturduk.
    #Üslerin görünmesi sağlandı.
    for exponent in combined_exp_list:       #Big(O)-O(1)    T(n)=c*n
        combined_coeff_list.append(exponent_coefficient_dict.get(exponent, 0))

    #Polinomların farkının yazdırılmasını sağlayan işlem.
    for i in range(len(combined_coeff_list)):     #Big(O)-O(N)
      print(combined_coeff_list[i], end = "")     #Zamansal Karmaşıklık:(c2+c3) + (c0 + c1)*n
      print("x^",combined_exp_list[i], end = "")
      if (i != len(combined_coeff_list)-1):
        print(" + ", end = "")

    print("\n", end = "")
    print("\n", end = "")
    print("[Katsayılar]            [Üsler]") 
    return (combined_coeff_list, combined_exp_list)


#Polinomların katsayılarını ve üslerini kullanıcıdan aldık.
coeff_1 = []
numbers = input('Please enter the coefficients of the first polynomial(,): ').split(',')
for entry in numbers:
    coeff_1.append(int(entry))

exp_1 = []
numbers = input('Please enter exponents of the first polynomial(,): ').split(',')
for entry in numbers:
    exp_1.append(int(entry))


coeff_2 = []
numbers = input('Please enter the coefficients of the second polynomial(,): ').split(',')
for entry in numbers:
    coeff_2.append(int(entry))


exp_2 = []
numbers = input('Please enter exponents of the second polynomial(,): ').split(',')
for entry in numbers:
    exp_2.append(int(entry))

print("\n", end = "")
print("###############################################################")
print("\n", end = "")  

#Katsayı listelerinin uzunluklarını tanımladık.
m = len(coeff_1) 
n = len(coeff_2)

#Oluşturulan polinomların yazdırılması.
#Toplama ve Çıkarma işlemlerinin sonuçlarının yazdırılıp oluşan katsayı ve üs değerlerinin liste halinde gösterilmesi.
print("First polynomial is") 
printPoly(coeff_1,m)
print("\n", end = "") 
print("Second polynomial is") 
printPoly1(coeff_2, n)
print("\n", end = "") 
print("-------------------------------")
print("(+)Sum of Polynomials")
print(add_coefficient(exp_1, coeff_1, exp_2, coeff_2))
print("\n", end = "")
print("(-)Difference of Polynomials")
print(dif_coefficient(exp_1, coeff_1, exp_2, coeff_2))

