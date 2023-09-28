import json

def create_post(post_name,post_title,post_beta,post_img,post_img_created,post_discription):
    with open('Title_database.josn','a') as file:
        data = {'post_name':post_name,'post_title':post_title,'post_beta':post_beta,'post_img':post_img,'post_img_created':post_img_created,'post_discription':post_discription}
        json.dump(data,file)
        file.write('\n')
        file.read('"post_name" :" Uzum Market","post_beta" : "16:44 / 25.09.2023","post_title " : "Uzum Market етакчиликни мустаҳкамламоқда: мамлакат аҳолисининг 80% дан ортиғи миллий маркетплейсни билади","post_img " : "https://storage.kun.uz/source/9/4JHNmU37i4igngC0V3dGHpZB7x3h49ho.jpg", "post_img_created" : "Фото: Uzum Market" , "post_discription" : """Research Group Central Asia кенг кўламли тадқиқоти доирасида сўровда қатнашган ҳар иккинчи ўзбекистонлик Uzum Market миллий маркетплейсида харид қилган, 40 фоизи эса ўтган ой давомида Uzum Market’да буюртма берган.RGC тадқиқот агентлиги мамлакат аҳолиси онлайн харид қилиш учун қайси иловаларни танлашини, кўпинча онлайн буюртма берилишини ва онлайн харид қилиш платформасини танлашда нималарга эътибор беришларини аниқлаш учун Ўзбекистонда жадал ривожланаётган e-commercе бозорини ўрганиб чиқди. Тадқиқотда 18 ёшдан 54 ёшгача бўлган 800 дан ортиқ ўзбекистонлик иштирок этди — танлама бутун мамлакат аҳолисининг вакиллик қилиши учун тузилган. РГCА мунтазам равишда турли соҳаларда фойдаланувчи хатти-ҳаракатлари бўйича тадқиқотлар олиб боради, бу эса ўзбекистонликларнинг одатларидаги ўзгаришларни динамикада баҳолашга имкон беради.Сўнгги ойларда Uzum Market миллий маркетплейси ҳақида билиш сезиларли даражада ошди — респондентларнинг 83 фоизи онлайн харид қилиш учун илова ва сервислар орасида маркетплейс ҳақида айтишади, 56 фоизи эса биринчи ўринда миллий платформа ҳақида эслайди. Шу билан бирга, Uzum Market пойтахтда ҳам, минтақаларда ҳам етакчиликни мустаҳкамламоқда. Узоқ вақт давомида ўзбекистонликларнинг танлови учун курашда асосий рақобатчилар бўлиб келган ОLX ва Telegram ўз позицияларини сезиларли даражада йўқотмоқда — респондентларнинг атиги 43 фоизи ва 32 фоизи уларни айтишди. Телеграм мессенжерида харидларни мамлакатнинг ҳар тўртинчи аҳолиси амалга оширган, ОLX иловасидан эса ўзбекистонликларнинг 23 фоизи харид қилиш учун фойдаланган.— Тадқиқот доирасида биз учун нафақат танловнинг ўзгаришларни, балки мамлакат аҳолиси   у ёки бу сайтни танлашининг сабабларини ҳам аниқлаш муҳим, — дейди RGCА тадқиқот агентлиги директори Вячеслав Карпов. — Ва агар фойдали содиқлик дастури харид қилиш платформасини танлашда энг муҳим мезон бўлиб қолса, сўнгги бир неча ой ичида танлов ва тўлов қулайлигининг аҳамияти сезиларли даражада ошди, бу харидорлар орасида тажрибали фойдаланувчилар сонининг кўпайишини кўрсатади. Шунингдек, мезонларнинг юқори қисмида кутиганидек тезкор етказиб бериш ва арзон нархлар. Uzum Market ўз ассортименти ва 1 кун ичида етказиб бериш билан айнан шу ва бошқа мезонларга тўғри келгани сабабли, унинг барча ёш тоифаларида ўзбекистонликлар орасида машҳурлиги ортиб бормоқда.Эслатиб ўтамиз, ярим йил олдин, жорий йилнинг март ойида сўровда қатнашганларнинг ярмидан кўпи (52%) Uzum Market брендини, харид қилиш платформалари орасида OLX иловасини 58% респондентлар, Telegram’ни эса 53% ўзбекистонликлар айтишган.Компания ҳақида. Research Group Central Asia 2022 йил бошида истеъмолчи тадқиқотлари бозорида тўлиқ хизмат кўрсатувчи агентлик сифатида ташкил этилган. RGCА бу — биринчи навбатда, тадқиқот лойиҳаларини амалга оширишда катта тажрибага эга бўлган мутахассислардир. Компания миқдорий ва сифатли тадқиқотларнинг тўлиқ спектрини олиб боради, IPSOS халқаро операторининг расмий аккредитациядан ўтган агентлиги, шунингдек "Romir" тадқиқот ҳолдингининг лицензиати ҳисобланади.')
        

def load_database():
    try:
        with open('Title_database.json','r') as file :
            lines =  file.readlines()
            database = [json.loads(line) for line in lines] 
            return database
    except FileNotFoundError :
        return []         
def get_user_input ():
    user_input = input("Enter the name of news: ")         
    return user_input
    
def ask_news(user_input, database):
    for entry in database:
        if entry['post_name'] == user_input:
            return entry['post_name']
            
def main():        
    while True:
        database = load_database()
        user_input = get_user_input()
        news = ask_news(user_input,database)
        if news:
            print(news)
            break
        else:
            print("Sorry, I don't found this news , if  you want to enter :")
            post_name = input("Enter name of the news: ") 
            post_beta = input("Enter the post_title: ")    
            post_title = input("Enter the post_beta:")  
            post_img = input("Enter the post_img:")  
            post_img_created = input("Enter the who created post_img:") 
            post_discription = input("Enter the discription about post:") 
            create_post(post_name,post_title,post_beta,post_img,post_img_created,post_discription)
            print("Okay I saved new information")

            continue_prompt = input("Again do you have info about news yes/no")
            if continue_prompt.lower() == 'n':
                continue

if __name__ == '__main__'   :
    main()

             


