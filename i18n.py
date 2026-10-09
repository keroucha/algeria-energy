"""النصوص بثلاث لغات + إعدادات البحث عن الأخبار لكل لغة."""

LANGS = {"ar": "العربية", "fr": "Français", "en": "English"}
DEFAULT_LANG = "ar"
RTL = {"ar"}

TEXT = {
    "ar": {
        "desc": "تابع آخر أخبار الطاقات المتجددة في الجزائر: الطاقة الشمسية، طاقة الرياح، الهيدروجين الأخضر ومشاريع سونلغاز، بالعربية والفرنسية والإنجليزية.",
        "about": "موقع يجمع لك أحدث أخبار الطاقات المتجددة في الجزائر: محطات الطاقة الشمسية، طاقة الرياح، الهيدروجين الأخضر، والبرنامج الوطني لبلوغ 15 غيغاواط. سجّل بريدك لتطّلع على الأخبار بلغتك المفضلة.",
        "title": "الطاقات المتجددة في الجزائر",
        "subtitle": "سجّل دخولك لتطّلع على آخر مستجدات الانتقال الطاقوي",
        "lang": "اللغة", "email": "البريد الإلكتروني", "submit": "ادخل واطّلع على الأخبار",
        "bad_email": "من فضلك أدخل بريداً إلكترونياً صحيحاً.",
        "too_many": "محاولات كثيرة، حاول لاحقاً.",
        "bad_token": "انتهت صلاحية الصفحة، أعد المحاولة.",
        "news_title": "آخر أخبار الطاقات المتجددة في الجزائر",
        "welcome": "مرحباً بك", "source": "المصدر", "back": "العودة",
        "live": "أخبار محدّثة تلقائياً", "offline": "تعذّر جلب الأخبار الحية الآن، هذه أبرز العناوين المحفوظة.",
        "footer": "موقع إخباري مستقل حول الطاقات المتجددة في الجزائر",
    },
    "fr": {
        "desc": "Suivez l'actualité des énergies renouvelables en Algérie : solaire, éolien, hydrogène vert et projets Sonelgaz, en arabe, français et anglais.",
        "about": "Ce site rassemble les dernières actualités des énergies renouvelables en Algérie : centrales solaires, éolien, hydrogène vert et programme national de 15 GW. Inscrivez-vous pour lire les actualités dans votre langue.",
        "title": "Énergies renouvelables en Algérie",
        "subtitle": "Inscrivez-vous pour suivre l'actualité de la transition énergétique",
        "lang": "Langue", "email": "Adresse e-mail", "submit": "Accéder aux actualités",
        "bad_email": "Veuillez saisir une adresse e-mail valide.",
        "too_many": "Trop de tentatives, réessayez plus tard.",
        "bad_token": "Page expirée, veuillez réessayer.",
        "news_title": "Dernières actualités des énergies renouvelables en Algérie",
        "welcome": "Bienvenue", "source": "Source", "back": "Retour",
        "live": "Actualités mises à jour automatiquement",
        "offline": "Impossible de charger les actualités en direct, voici les titres enregistrés.",
        "footer": "Site d'information indépendant sur les énergies renouvelables en Algérie",
    },
    "en": {
        "desc": "Follow the latest renewable energy news in Algeria: solar, wind, green hydrogen and Sonelgaz projects, in Arabic, French and English.",
        "about": "This site gathers the latest renewable energy news in Algeria: solar plants, wind power, green hydrogen and the national 15 GW programme. Sign in with your email to read the news in your language.",
        "title": "Renewable Energy in Algeria",
        "subtitle": "Sign in to follow the latest on the energy transition",
        "lang": "Language", "email": "Email address", "submit": "Enter and read the news",
        "bad_email": "Please enter a valid email address.",
        "too_many": "Too many attempts, please try later.",
        "bad_token": "Page expired, please try again.",
        "news_title": "Latest renewable energy news in Algeria",
        "welcome": "Welcome", "source": "Source", "back": "Back",
        "live": "Automatically updated news",
        "offline": "Live news is unavailable right now; here are the saved headlines.",
        "footer": "Independent news site on renewable energy in Algeria",
    },
}

# استعلام Google News RSS لكل لغة
NEWS_QUERY = {
    "ar": ("الطاقات المتجددة الجزائر", "ar", "DZ", "DZ:ar"),
    "fr": ("énergies renouvelables Algérie", "fr", "DZ", "DZ:fr"),
    "en": ("renewable energy Algeria", "en", "DZ", "DZ:en"),
}

# عناوين احتياطية إذا فشل الاتصال بالإنترنت
FALLBACK_NEWS = {
    "ar": [
        ("برنامج 3000 ميغاواط شمسي ضمن هدف 15 غيغاواط", "https://attaqa.net/?p=565317", "منصة الطاقة"),
        ("محطة تندلة بالمغير أول محطة في مرحلة التنفيذ", "https://attaqa.net/?p=566459", "منصة الطاقة"),
        ("قانون المالية 2026 يفتح الاستثمار في الطاقات المتجددة", "https://news.radioalgerie.dz/ar/node/83361", "إذاعة الجزائر"),
    ],
    "fr": [
        ("Programme solaire de 3000 MW dans l'objectif de 15 GW", "https://attaqa.net/?p=565317", "Attaqa"),
        ("Centrale de Tindla : première en phase de réalisation", "https://attaqa.net/?p=566459", "Attaqa"),
        ("Loi de finances 2026 : ouverture à l'investissement", "https://news.radioalgerie.dz/ar/node/83361", "Radio Algérie"),
    ],
    "en": [
        ("3,000 MW solar programme within a 15 GW target", "https://attaqa.net/?p=565317", "Attaqa"),
        ("Tindla plant first to enter construction", "https://attaqa.net/?p=566459", "Attaqa"),
        ("2026 Finance Law opens renewables investment", "https://news.radioalgerie.dz/ar/node/83361", "Radio Algérie"),
    ],
}
