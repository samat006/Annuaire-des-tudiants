from flask import Flask, render_template

app = Flask(__name__)

students = [{
        "id": 2,
        "name": "Abdou Samath Seck",
        "major": "Data Engineer",
        "year": "M2",
        "photo": "/static/abdou.png",
        "email": "abdou.seck@example.com",
        "bio": """Hello,

My name is Abdou Samath Seck. I am 25 years old. I am from Dakar, SENEGAL. I am a data engineer. I like coding very much.

My coding strengths are Python and SQL. I can make scripts to work with data. I can also use tools like Pandas and Excel. I am good at cleaning data and making small programs.

My coding weaknesses are that I am not very good in English and in big projects. I need more practice in cloud tools like AWS and big data tools like Spark. I also need to learn more about programming in Java and web tools.

My biggest achievement in coding is that I made a small program to clean and analyze data for a school project. The program worked well and helped my friends understand the data. I was very happy because I learned a lot and the project was successful.

My future plans are to learn more about data engineering. I want to work with big data and cloud tools. I want to make programs that help companies use data better. I also want to improve my English for work.

A fun fact about me is that I like solving puzzles. I sometimes make small coding games for fun. I like learning new things and trying new tools.

Thank you for reading my evaluation. I want to learn more and become a better data engineer."""
,
        "age": 25,
        "nationality": "Sénégalaise",
        "phone": "+33 6 23 45 67 89",
        "city": "Corte",
        "skills": ["Python", "Spark", "Hadoop", "SQL", "Kafka", "Airflow", "Machine Learning", "GCP"]
    },
    {
        "id": 1,
        "name": "GHOULAM Mehdi",
        "major": "Développeur",
        "year": "M2",
        "photo": "/static/med-pp.png",
        "email": "mehdi.ghoulam@example.com",
        "bio": "Intéressé par le développement web, mobile et le cloud. Passionné par les technologies modernes et l'innovation.",
        "age": 24,
        "nationality": "Française",
        "phone": "+33 6 12 34 56 78",
        "city": "Paris",
        "skills": ["JavaScript", "React", "Node.js", "Python", "AWS", "Docker", "Flutter"]
    },
    
    {
        "id": 3,
        "name": "ABBOURI Hafousti",
        "major": "Data Engineer",
        "year": "M2",
        "photo": "/static/Hafsa_pic.jpeg",
        "email": "hafousti.abbouri@example.com",
        "bio": "Intéressée par les architectures data, l'optimisation de traitements et l'ingénierie des données. Spécialisée dans les solutions cloud et le Big Data.",
        "age": 23,
        "nationality": "Marocaine",
        "phone": "+33 6 34 56 78 90",
        "city": "Marseille",
        "skills": ["Python", "SQL", "ETL", "Azure", "Databricks", "Power BI", "Snowflake"]
    },
    {
        "id": 18,
        "name": "Manal",
        "major": "Informatique",
        "year": "M2",
        "photo": "/static/manal.png",
        "email": "manal@example.com",
        "bio": "Passionnée par le full stack. Aime créer des applications web complètes et performantes avec des interfaces modernes.",
        "age": 24,
        "nationality": "Française",
        "phone": "+33 6 45 67 89 01",
        "city": "Toulouse",
        "skills": ["React", "Vue.js", "Node.js", "MongoDB", "Express", "TypeScript", "Tailwind CSS"]
    },
    {
        "id": 17,
        "name": "ROBLES Nicolas",
        "major": "Full Stack",
        "year": "M2",
        "photo": "/static/nicola.jpg",
        "email": "nicolas.robles@example.com",
        "bio": "S'intéresse au développement web, aux API et à l'intégration frontend. Expert en architecture microservices et RESTful API.",
        "age": 26,
        "nationality": "Espagnole",
        "phone": "+33 6 56 78 90 12",
        "city": "Bordeaux",
        "skills": ["JavaScript", "React", "REST API", "GraphQL", "PostgreSQL", "Docker", "Next.js"]
    },
    {
        "id": 4,
        "name": "Clémentine",
        "major": "Data Engineer",
        "year": "M2",
        "photo": "/static/clementine.png",
        "email": "clementine@example.com",
        "bio": "Passionnée par la data, le machine learning et les solutions cloud. Spécialisée dans l'intelligence artificielle et l'analyse prédictive.",
        "age": 23,
        "nationality": "Française",
        "phone": "+33 6 67 89 01 23",
        "city": "Nantes",
        "skills": ["Python", "Scikit-learn", "TensorFlow", "AWS", "Spark", "SQL", "Pandas"]
    },
    {
        "id": 5,
        "name": "EL MOURABIT Badre",
        "major": "Full Stack",
        "year": "M2",
        "photo": "/static/badre.png",
        "email": "badre.elmourabit@example.com",
        "bio": "Intéressé par le développement web, l'intégration d'API et les technologies modernes. Passionné par l'architecture logicielle et les bonnes pratiques.",
        "age": 25,
        "nationality": "Marocaine",
        "phone": "+33 6 78 90 12 34",
        "city": "Nice",
        "skills": ["Angular", "Java", "Spring Boot", "MySQL", "Redis", "Kubernetes", "Jenkins"]
    },
    {
        "id": 6,
        "name": "DAHDOUH Ahmed",
        "major": "Full Stack",
        "year": "M2",
        "photo": "/static/dahdouh-ahmed.jpg",
        "email": "ahmed.dahdouh@example.com",
        "bio": "Développeur Full Stack avec intérêt pour les interfaces frontend et les services backend. Expert en développement d'applications web modernes et scalables.",
        "age": 24,
        "nationality": "Tunisienne",
        "phone": "+33 6 89 01 23 45",
        "city": "Strasbourg",
        "skills": ["React", "Django", "Python", "PostgreSQL", "Git", "CI/CD", "Material-UI"]
    },
    {
        "id": 7,
        "name": "CATTAROSSI DARTIGUELONGUE Thomas",
        "major": "Full Stack",
        "year": "M2",
        "photo": "/static/thomas-c.png",
        "email": "thomas.cattarossi@example.com",
        "bio": "Passionné de développement full stack et de création de solutions web fonctionnelles. Aime travailler sur des projets innovants et challengeants.",
        "age": 25,
        "nationality": "Française",
        "phone": "+33 6 90 12 34 56",
        "city": "Lille",
        "skills": ["Vue.js", "Node.js", "Express", "MongoDB", "Jest", "Webpack", "SASS"]
    },
    {
        "id": 8,
        "name": "BESSAM Mounia",
        "major": "Full Stack",
        "year": "M2",
        "photo": "/static/mounia.png",
        "email": "mounia.bessam@example.com",
        "bio": "Intéressée par les technologies web, le responsive design et l'expérience utilisateur. Spécialisée en UX/UI et développement frontend moderne.",
        "age": 23,
        "nationality": "Algérienne",
        "phone": "+33 7 01 23 45 67",
        "city": "Montpellier",
        "skills": ["HTML/CSS", "JavaScript", "React", "Figma", "Tailwind CSS", "UX/UI", "Svelte"]
    },
    {
        "id": 9,
        "name": "THIRY Stephane",
        "major": "Full Stack",
        "year": "M2",
        "photo": "/static/stephane.png",
        "email": "stephane.thiry@example.com",
        "bio": "Développeur full stack aimant travailler sur la conception d'applications complètes. Passionné par les technologies PHP et les frameworks modernes.",
        "age": 27,
        "nationality": "Belge",
        "phone": "+33 7 12 34 56 78",
        "city": "Rennes",
        "skills": ["PHP", "Laravel", "MySQL", "Vue.js", "Docker", "Linux", "Composer"]
    },
    {
        "id": 10,
        "name": "LOVICHI Dorian",
        "major": "Full Stack",
        "year": "M2",
        "photo": "/static/dorian.png",
        "email": "dorian.lovichi@example.com",
        "bio": "Passionné de développement web, d'API et d'applications modernes. Expert en TypeScript et architectures event-driven.",
        "age": 24,
        "nationality": "Française",
        "phone": "+33 7 23 45 67 89",
        "city": "Grenoble",
        "skills": ["React", "TypeScript", "NestJS", "PostgreSQL", "GraphQL", "AWS", "Prisma"]
    },
    {
        "id": 11,
        "name": "KILIMOU Pouwedeou Ambroise",
        "major": "Data Engineer",
        "year": "M2",
        "photo": "/static/ambroise.png",
        "email": "ambroise.kilimou@example.com",
        "bio": "S'intéresse aux pipelines de données, au traitement Big Data et au cloud. Spécialisé dans l'ingestion et le traitement de données massives en temps réel.",
        "age": 26,
        "nationality": "Togolaise",
        "phone": "+33 7 34 56 78 90",
        "city": "Orléans",
        "skills": ["Python", "Spark", "Hadoop", "Kafka", "Elasticsearch", "Docker", "Flink"]
    },
    {
        "id": 12,
        "name": "MAHAM BOWBA Youssouf",
        "major": "Data Engineer",
        "year": "M2",
        "photo": "/static/youssouf.png",
        "email": "youssouf.maham@example.com",
        "bio": "Passionné par l'ingénierie des données, l'ETL et la visualisation. Expert en business intelligence et data visualization.",
        "age": 25,
        "nationality": "Tchadienne",
        "phone": "+33 7 45 67 89 01",
        "city": "Tours",
        "skills": ["Python", "SQL", "Tableau", "Power BI", "Azure", "ETL", "DAX"]
    },
    {
        "id": 13,
        "name": "MARCHISELLI Anthony",
        "major": "Full Stack",
        "year": "M2",
        "photo": "/static/anthony-m.png",
        "email": "anthony.marchiselli@example.com",
        "bio": "Développeur full stack, aime travailler sur le backend et l'optimisation. Spécialisé en architecture microservices et optimisation de performances.",
        "age": 24,
        "nationality": "Italienne",
        "phone": "+33 7 56 78 90 12",
        "city": "Angers",
        "skills": ["Java", "Spring", "React", "MySQL", "Redis", "Microservices", "RabbitMQ"]
    },
    {
        "id": 14,
        "name": "MENGHI Anthony",
        "major": "Full Stack",
        "year": "M2",
        "photo": "/static/anthony-me.png",
        "email": "anthony.menghi@example.com",
        "bio": "Intéressé par le développement web, les API et les technologies modernes. Passionné par les applications temps réel et les WebSockets.",
        "age": 23,
        "nationality": "Française",
        "phone": "+33 7 67 89 01 23",
        "city": "Dijon",
        "skills": ["JavaScript", "Node.js", "React", "MongoDB", "Express", "Socket.io", "WebRTC"]
    },
    {
        "id": 15,
        "name": "MICHELOZZI Matthieu",
        "major": "Data Engineer",
        "year": "M2",
        "photo": "/static/matthieu.png",
        "email": "matthieu.michelozzi@example.com",
        "bio": "Passionné par le traitement de données, la modélisation et le cloud. Expert en data warehousing et architecture de données moderne.",
        "age": 25,
        "nationality": "Française",
        "phone": "+33 7 78 90 12 34",
        "city": "Reims",
        "skills": ["Python", "Spark", "AWS", "Redshift", "SQL", "Data Modeling", "dbt"]
    },
    {
        "id": 16,
        "name": "POIRIER Achille",
        "major": "Full Stack",
        "year": "M2",
        "photo": "/static/achille.png",
        "email": "achille.poirier@example.com",
        "bio": "Développeur full stack, aime créer des applications performantes et modernes. Spécialisé en DevOps et déploiement continu.",
        "age": 26,
        "nationality": "Française",
        "phone": "+33 7 89 01 23 45",
        "city": "Le Havre",
        "skills": ["React", "Node.js", "TypeScript", "PostgreSQL", "Docker", "Kubernetes", "Terraform"]
    }
]


@app.route("/")
def index():
    return render_template("index.html", students=students)


@app.route("/student/<int:student_id>")
def student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    return render_template("student.html", student=student)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # PORT fourni par Render
    app.run(host="0.0.0.0", port=port, debug=True)
