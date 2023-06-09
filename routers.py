from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from settings import settings
from service.routers import router

services_router = APIRouter(prefix='')

templates = Jinja2Templates(directory=f'{settings.APP_PATH}/templates/')

# app.include_router(router=auth_router)
services_router.include_router(router=router)

supps: dict = {
    '10000': 'Юридические лица - коммерческие корпоративные организации',
    '11000': 'Хозяйственные товарищества',
    '11051': 'Полные товарищества',
    '11064': 'Товарищества на вере (коммандитные товарищества)',
    '12000': 'Хозяйственные общества',
    '12200': 'Акционерные общества',
    '12247': 'Публичные акционерные общества',
    '12267': 'Непубличные акционерные общества',
    '12300': 'Общества с ограниченной ответственностью',
    '13000': 'Хозяйственные партнерства',
    '14000': 'Производственные кооперативы (артели)',
    '14100': 'Сельскохозяйственные производственные кооперативы',
    '14153': 'Сельскохозяйственные артели (колхозы)',
    '14154': 'Рыболовецкие артели (колхозы)',
    '14155': 'Кооперативные хозяйства (коопхозы)',
    '14200': 'Производственные кооперативы',
    '15300': 'Крестьянские (фермерские) хозяйства',
    '19000': 'Юридические лица - прочие коммерческие организации',
    '20000': 'Юридические лица - некоммерческие корпоративные организации',
    '20100': 'Потребительские кооперативы',
    '20101': 'Гаражные и гаражно-строительные кооперативы',
    '20102': 'Жилищные или жилищно-строительные кооперативы',
    '20103': 'Жилищные накопительные кооперативы',
    '20104': 'Кредитные потребительские кооперативы',
    '20105': 'Кредитные потребительские кооперативы граждан',
    '20106': 'Кредитные кооперативы второго уровня',
    '20107': 'Потребительские общества',
    '20108': 'Общества взаимного страхования',
    '20109': 'Сельскохозяйственные потребительские перерабатывающие кооперативы',
    '20110': 'Сельскохозяйственные потребительские сбытовые (торговые) кооперативы',
    '20111': 'Сельскохозяйственные потребительские обслуживающие кооперативы',
    '20112': 'Сельскохозяйственные потребительские снабженческие кооперативы',
    '20113': 'Объединения фермерских хозяйств',
    '20115': 'Сельскохозяйственные потребительские животноводческие кооперативы',
    '20121': 'Фонды проката',
    '20200': 'Общественные организации',
    '20201': 'Политические партии',
    '20202': 'Профсоюзные организации',
    '20210': 'Общественные движения',
    '20211': 'Органы общественной самодеятельности',
    '20217': 'Территориальные общественные самоуправления',
    '20600': 'Ассоциации (союзы)',
    '20601': 'Ассоциации (союзы) экономического взаимодействия субъектов Российской Федерации',
    '20603': 'Советы муниципальных образований субъектов РФ',
    '20604': 'Союзы (ассоциации) кредитных кооперативов',
    '20605': 'Союзы (ассоциации) кооперативов',
    '20606': 'Союзы (ассоциации) общественных объединений',
    '20608': 'Союзы потребительских обществ',
    '20609': 'Адвокатские палаты',
    '20610': 'Нотариальные палаты',
    '20611': 'Торгово-промышленные палаты',
    '20612': 'Объединения работодателей',
    '20613': 'Объединения фермерских хозяйств',
    '20614': 'Некоммерческие партнерства',
    '20615': 'Адвокатские бюро',
    '20616': 'Коллегии адвокатов',
    '20619': 'Саморегулируемые организации',
    '20620': 'Объединения (ассоциации и союзы) благотворительных организаций',
    '20700': 'Товарищества собственников недвижимости',
    '20702': 'Садоводческие или огороднические некоммерческие товарищества',
    '20716': 'Товарищества собственников жилья',
    '21100': 'Казачьи общества',
    '21200': 'Общины коренных малочисленных народов РФ',
    '30000': 'Организации без прав юридического лица',
    '30001': 'Представительства юридических лиц',
    '30002': 'Филиалы юридических лиц',
    '30003': 'Обособленные подразделения юридических лиц',
    '30004': 'Структурные подразделения обособленных подразделений юридических лиц',
    '30005': 'Паевые инвестиционные фонды',
    '30006': 'Простые товарищества',
    '30008': 'Районные суды, городские суды, межрайонные суды (районные суды)',
    '40000': 'Международные организации на территории РФ',
    '40001': 'Межправительственные международные организации',
    '40002': 'Неправительственные международные организации',
    '50000': 'Физическое лицо',
    '50100': 'Организационно-правовые формы для коммерческой деятельности граждан',
    '50101': 'Главы крестьянских (фермерских) хозяйств',
    '50102': 'Индивидуальные предприниматели',
    '50200': 'Организационно-правовые формы для деятельности граждан, не отнесенной к предпринимательству',
    '50201': 'Адвокаты, учредившие адвокатский кабинет',
    '50202': 'Нотариусы, занимающиеся частной практикой',
    '60000': 'Юридические лица - коммерческие унитарные организации',
    '65000': 'Унитарные предприятия',
    '65100': 'Казенные предприятия',
    '65141': 'Федеральные казенные предприятия',
    '65142': 'Казенные предприятия субъектов РФ',
    '65143': 'Муниципальные казенные предприятия',
    '65200': 'Унитарные предприятия, основанные на праве хозяйственного ведения',
    '65241': 'Федеральные государственные унитарные предприятия',
    '65242': 'Государственные унитарные предприятия субъектов РФ',
    '65243': 'Муниципальные унитарные предприятия',
    '70000': 'Юридические лица - некоммерческие унитарные организации',
    '70400': 'Фонды',
    '70401': 'Благотворительные фонды',
    '70402': 'Негосударственные пенсионные фонды',
    '70403': 'Общественные фонды',
    '70404': 'Экологические фонды',
    '71400': 'Автономные некоммерческие организации',
    '71500': 'Религиозные организации',
    '71600': 'Публично-правовые компании',
    '71601': 'Государственные корпорации',
    '71602': 'Государственные компании',
    '71610': 'Отделения иностранных некоммерческих неправительственных организаций',
    '75000': 'Учреждения',
    '75100': 'Учреждения, созданные Российской Федерацией',
    '75101': 'Федеральные государственные автономные учреждения',
    '75103': 'Федеральные государственные бюджетные учреждения',
    '75104': 'Федеральные государственные казенные учреждения',
    '75200': 'Учреждения, созданные субъектом РФ',
    '75201': 'Государственные автономные учреждения субъектов РФ',
    '75203': 'Государственные бюджетные учреждения субъектов РФ',
    '75204': 'Государственные казенные учреждения субъектов РФ',
    '75300': 'Государственные академии наук',
    '75400': 'Муниципальные учреждения',
    '75401': 'Муниципальные автономные учреждения',
    '75403': 'Муниципальные бюджетные учреждения',
    '75404': 'Муниципальные казенные учреждения',
    '75500': 'Частные учреждения',
    '75502': 'Благотворительные учреждения',
    '75505': 'Общественные учреждения',
}

custs: dict = {
    '65143': 'Муниципальные казенные предприятия',
    '65243': 'Муниципальные унитарные предприятия',
    '75400': 'Муниципальные учреждения',
    '75401': 'Муниципальные автономные учреждения',
    '75403': 'Муниципальные бюджетные учреждения',
    '75404': 'Муниципальные казенные учреждения',
}

okpd = {
    '01': 'Продукция и услуги сельского хозяйства и охоты',
    '02': 'Продукция лесоводства, лесозаготовок и связанные с этим услуги',
    '03': 'Рыба и прочая продукция рыболовства и рыбоводства; услуги, связанные с рыболовством и рыбоводством',
    '05': 'Уголь',
    '06': 'Нефть и газ природный',
    '07': 'Руды металлические',
    '08': 'Продукция горнодобывающих производств прочая',
    '09': 'Услуги в области добычи полезных ископаемых',
    '10': 'Продукты пищевые',
    '11': 'Напитки',
    '12': 'Изделия табачные',
    '13': 'Текстиль и изделия текстильные',
    '14': 'Одежда',
    '15': 'Кожа и изделия из кожи',
    '16': 'Древесина и изделия из дерева и пробки, кроме мебели; изделия из соломки и материалов для плетения',
    '17': 'Бумага и изделия из бумаги',
    '18': 'Услуги печатные и услуги по копированию звуко- и видеозаписей, а также программных средств',
    '19': 'Кокс и нефтепродукты',
    '20': 'Вещества химические и продукты химические',
    '21': 'Средства лекарственные и материалы, применяемые в медицинских целях',
    '22': 'Изделия резиновые и пластмассовые',
    '23': 'Продукты минеральные неметаллические прочие',
    '24': 'Металлы основные',
    '25': 'Изделия металлические готовые, кроме машин и оборудования',
    '26': 'Оборудование компьютерное, электронное и оптическое',
    '27': 'Оборудование электрическое',
    '28': 'Машины и оборудование, не включенные в другие группировки',
    '29': 'Средства автотранспортные, прицепы и полуприцепы',
    '30': 'Средства транспортные и оборудование, прочие',
    '31': 'Мебель',
    '32': 'Изделия готовые прочие',
    '33': 'Услуги по ремонту и монтажу машин и оборудования',
    '35': 'Электроэнергия, газ, пар и кондиционирование воздуха',
    '36': 'Вода природная; услуги по очистке воды и водоснабжению',
    '37': 'Услуги по водоотведению; шлам сточных вод',
    '38': 'Услуги по сбору, обработке и удалению отходов; услуги по утилизации отходов',
    '39': 'Услуги по рекультивации и прочие услуги по утилизации отходов',
    '41': 'Здания и работы по возведению зданий',
    '42': 'Сооружения и строительные работы в области гражданского строительства',
    '43': 'Работы строительные специализированные',
    '45': 'Услуги по оптовой и розничной торговле и услуги по ремонту автотранспортных средств и мотоциклов',
    '46': 'Услуги по оптовой торговле, кроме оптовой торговли автотранспортными средствами и мотоциклами',
    '47': 'Услуги по розничной торговле, кроме розничной торговли автотранспортными средствами и мотоциклами',
    '49': 'Услуги сухопутного и трубопроводного транспорта',
    '50': 'Услуги водного транспорта',
    '51': 'Услуги воздушного и космического транспорта',
    '52': 'Услуги по складированию и вспомогательные транспортные услуги',
    '53': 'Услуги почтовой связи и услуги курьерские',
    '55': 'Услуги по предоставлению мест для временного проживания',
    '56': 'Услуги общественного питания',
    '58': 'Услуги издательские',
    '59': 'Услуги по производству кинофильмов, видеофильмов и телевизионных программ, звукозаписей и изданию музыкальных записей',
    '60': 'Услуги в области теле- и радиовещания',
    '61': 'Услуги телекоммуникационные',
    '62': 'Продукты программные и услуги по разработке программного обеспечения; консультационные и аналогичные услуги в области информационных технологий',
    '63': 'Услуги в области информационных технологий',
    '64': 'Услуги финансовые, кроме услуг по страхованию и пенсионному обеспечению',
    '65': 'Услуги по страхованию, перестрахованию и негосударственному пенсионному обеспечению, кроме обязательного социального обеспечения',
    '66': 'Услуги вспомогательные, связанные с услугами финансового посредничества и страхования',
    '68': 'Услуги по операциям с недвижимым имуществом',
    '69': 'Услуги юридические и бухгалтерские',
    '70': 'Услуги головных офисов; услуги консультативные в области управления предприятием',
    '71': 'Услуги в области архитектуры и инженерно-технического проектирования, технических испытаний, исследований и анализа',
    '72': 'Услуги и работы, связанные с научными исследованиями и экспериментальными разработками',
    '73': 'Услуги рекламные и услуги по исследованию конъюнктуры рынка',
    '74': 'Услуги профессиональные, научные и технические, прочие',
    '75': 'Услуги ветеринарные',
    '77': 'Услуги по аренде и лизингу',
    '78': 'Услуги по трудоустройству и подбору персонала',
    '79': 'Услуги туристических агентств, туроператоров и прочие услуги по бронированию и сопутствующие им услуги',
    '80': 'Услуги по обеспечению безопасности и проведению расследований',
    '81': 'Услуги по обслуживанию зданий и территорий',
    '82': 'Услуги в области административного, хозяйственного и прочего вспомогательного обслуживания',
    '84': 'Услуги в области государственного управления и обеспечения военной безопасности, услуги в области обязательного социального обеспечения',
    '85': 'Услуги в области образования',
    '86': 'Услуги в области здравоохранения',
    '87': 'Услуги по предоставлению ухода с обеспечением проживания',
    '88': 'Услуги социальные без обеспечения проживания',
    '90': 'Услуги в области творчества, искусства и развлечений',
    '91': 'Услуги библиотек, архивов, музеев и прочие услуги в области культуры',
    '92': 'Услуги по организации и проведению азартных игр и заключению пари, лотерей',
    '93': 'Услуги, связанные со спортом, и услуги по организации развлечений и отдыха',
    '94': 'Услуги общественных организаций',
    '95': 'Услуги по ремонту компьютеров, предметов личного потребления и бытовых товаров',
    '96': 'Услуги персональные прочие',
    '97': 'Услуги домашних хозяйств с наемными работниками',
    '98': 'Продукция и различные услуги частных домашних хозяйств для собственных нужд',
    '99': 'Услуги, предоставляемые экстерриториальными организациями и органами'
}


@services_router.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('index.html', {
        'request': request,
        'supps': supps,
        'custs': custs,
        'okpd': okpd,
    })
