from django.core.management.base import BaseCommand
from careers.models import Career

# Illustrative exploration data. Verify official eligibility/admission requirements
# for the relevant board, state, institution and admission year before production.
SEED = [
    {
        "title": "Software Developer", "sector": "Technology",
        "description": "Designs, builds, tests and maintains software applications.",
        "interests": ["technology", "problem_solving", "creativity"],
        "skills": ["Programming", "Debugging", "Teamwork"],
        "pathways": [
            "After Class 10: consider Class 11–12 with Mathematics and Computer Science where offered, or an eligible polytechnic diploma.",
            "After Class 12: explore B.E./B.Tech Computer Science, BCA, B.Sc Computer Science or other eligible computing programs.",
            "Build programming projects, learn data structures and practise collaboration."
        ],
        "subjects": ["Mathematics", "Computer Science"],
        "source_verified": False,
    },
    {
        "title": "Data Scientist", "sector": "Data and AI",
        "description": "Uses statistics, programming and domain knowledge to analyse data and build models.",
        "interests": ["mathematics", "technology", "problem_solving", "research"],
        "skills": ["Statistics", "Python", "Data analysis", "Communication"],
        "pathways": [
            "After Class 10: a mathematics-focused subject combination is useful; compare available Science and other eligible routes.",
            "After Class 12: explore eligible degrees in Statistics, Mathematics, Computer Science, Data Science or Engineering.",
            "Learn Python, statistics, SQL and data visualisation; create small data projects."
        ],
        "subjects": ["Mathematics", "Computer Science", "Statistics"],
        "source_verified": False,
    },
    {
        "title": "AI / Machine Learning Engineer", "sector": "Artificial Intelligence",
        "description": "Develops and evaluates software systems that use machine learning and AI.",
        "interests": ["technology", "mathematics", "problem_solving", "research"],
        "skills": ["Python", "Mathematics", "Machine learning", "Software engineering"],
        "pathways": [
            "After Class 10: explore Mathematics and computing subjects where available.",
            "After Class 12: investigate eligible Computer Science, AI/ML, Data Science, Mathematics or related degrees.",
            "Build foundations in coding, statistics, algorithms and responsible AI."
        ],
        "subjects": ["Mathematics", "Computer Science", "Statistics"],
        "source_verified": False,
    },
    {
        "title": "Cybersecurity Analyst", "sector": "Cybersecurity",
        "description": "Helps protect systems, networks and information from security threats.",
        "interests": ["technology", "problem_solving", "research", "detail"],
        "skills": ["Networking", "Operating systems", "Security basics", "Critical thinking"],
        "pathways": [
            "After Class 10: consider a computing-focused school or diploma route available to you.",
            "After Class 12 or diploma: research eligible Computer Science, IT, Cybersecurity or related qualifications.",
            "Practise only in legal training labs and learn networking, Linux and secure coding."
        ],
        "subjects": ["Computer Science", "Mathematics"],
        "source_verified": False,
    },
    {
        "title": "Doctor / Physician", "sector": "Healthcare",
        "description": "Diagnoses, treats and helps prevent illness; regulated qualifications and registration are required.",
        "interests": ["biology", "helping_people", "research", "problem_solving"],
        "skills": ["Biology", "Communication", "Careful decision-making"],
        "pathways": [
            "After Class 10: investigate a Science combination with the required Biology and other subjects.",
            "After Class 12: verify current NEET-UG and medical-course requirements from official authorities.",
            "Complete an approved qualification and required registration; other healthcare careers have different routes."
        ],
        "subjects": ["Biology", "Chemistry", "Physics"],
        "source_verified": False,
    },
    {
        "title": "Nurse", "sector": "Healthcare",
        "description": "Provides patient care and health education in hospitals, clinics and communities.",
        "interests": ["biology", "helping_people", "communication", "detail"],
        "skills": ["Patient care", "Communication", "Teamwork", "Clinical knowledge"],
        "pathways": [
            "After Class 10: compare recognised school and vocational options; check each nursing course's eligibility.",
            "After Class 12 or another eligible route: investigate recognised nursing programs such as B.Sc Nursing or diploma programs.",
            "Verify current admission and registration requirements with official nursing authorities."
        ],
        "subjects": ["Biology", "Chemistry", "English"],
        "source_verified": False,
    },
    {
        "title": "Pharmacist", "sector": "Healthcare",
        "description": "Works with medicines, their safe use and patient counselling under applicable professional rules.",
        "interests": ["biology", "chemistry", "helping_people", "detail"],
        "skills": ["Chemistry", "Accuracy", "Communication", "Medicine safety"],
        "pathways": [
            "After Class 10: check the Science subjects required by the pharmacy programs you may target.",
            "After Class 12 or another eligible route: compare D.Pharm, B.Pharm and current eligibility rules.",
            "Confirm course approval and registration requirements with official pharmacy authorities."
        ],
        "subjects": ["Chemistry", "Biology", "Physics", "Mathematics"],
        "source_verified": False,
    },
    {
        "title": "Physiotherapist", "sector": "Healthcare",
        "description": "Helps people improve movement, function and recovery through rehabilitation.",
        "interests": ["biology", "helping_people", "problem_solving", "communication"],
        "skills": ["Anatomy", "Communication", "Observation", "Rehabilitation"],
        "pathways": [
            "After Class 10: explore Science subjects and compare requirements for recognised physiotherapy programs.",
            "After Class 12: research approved Bachelor of Physiotherapy programs and current admission rules.",
            "Check institution recognition, clinical training and registration requirements."
        ],
        "subjects": ["Biology", "Physics", "Chemistry"],
        "source_verified": False,
    },
    {
        "title": "Veterinarian", "sector": "Animal Health",
        "description": "Provides medical care for animals and supports animal health and welfare.",
        "interests": ["biology", "helping_people", "research", "building"],
        "skills": ["Biology", "Animal care", "Observation", "Communication"],
        "pathways": [
            "After Class 10: explore Science combinations that include the required subjects.",
            "After Class 12: check current veterinary degree eligibility and admission rules from official authorities.",
            "Complete an approved veterinary qualification and applicable registration."
        ],
        "subjects": ["Biology", "Chemistry", "Physics"],
        "source_verified": False,
    },
    {
        "title": "Chartered Accountant", "sector": "Finance",
        "description": "Works in accounting, audit, taxation, finance and business advisory.",
        "interests": ["business", "mathematics", "problem_solving", "detail"],
        "skills": ["Accounting", "Analysis", "Ethics", "Communication"],
        "pathways": [
            "After Class 10: explore Commerce, though students should verify the professional body's current entry rules.",
            "After Class 12: review the current ICAI entry route, examinations and practical training requirements.",
            "Develop accounting, spreadsheet, communication and ethical decision-making skills."
        ],
        "subjects": ["Accountancy", "Business Studies", "Economics", "Mathematics"],
        "source_verified": False,
    },
    {
        "title": "Accountant / Finance Executive", "sector": "Finance",
        "description": "Maintains financial records, supports reporting and helps organisations understand costs and performance.",
        "interests": ["business", "mathematics", "detail", "problem_solving"],
        "skills": ["Accounting", "Spreadsheets", "Accuracy", "Communication"],
        "pathways": [
            "After Class 10: compare Commerce and other available streams based on interests and local options.",
            "After Class 12: explore eligible B.Com, finance, accounting or related qualifications.",
            "Practise spreadsheets, bookkeeping, analysis and professional communication."
        ],
        "subjects": ["Accountancy", "Business Studies", "Economics"],
        "source_verified": False,
    },
    {
        "title": "Business Manager", "sector": "Business",
        "description": "Coordinates people, projects and resources to help an organisation meet its goals.",
        "interests": ["business", "communication", "leadership", "problem_solving"],
        "skills": ["Planning", "Communication", "Data literacy", "Teamwork"],
        "pathways": [
            "After Class 10: compare Commerce, Humanities, Science and vocational routes; several routes can lead to business study.",
            "After Class 12: explore eligible BBA, B.Com, Economics or other degrees.",
            "Build project, teamwork, communication and analytical skills."
        ],
        "subjects": ["Business Studies", "Economics", "Mathematics", "English"],
        "source_verified": False,
    },
    {
        "title": "Entrepreneur", "sector": "Business",
        "description": "Identifies a problem or opportunity and builds a product, service or organisation.",
        "interests": ["business", "creativity", "leadership", "problem_solving"],
        "skills": ["Planning", "Customer research", "Finance", "Experimentation"],
        "pathways": [
            "After Class 10: any suitable stream may be relevant depending on the business idea.",
            "After Class 12: explore business, design, technology or domain-specific courses as useful.",
            "Try supervised small projects, learn budgeting and talk to trusted mentors."
        ],
        "subjects": ["Business Studies", "Economics", "Mathematics", "Computer Science"],
        "source_verified": False,
    },
    {
        "title": "Economist", "sector": "Economics and Policy",
        "description": "Studies how people, organisations and governments make choices about resources.",
        "interests": ["mathematics", "research", "business", "problem_solving"],
        "skills": ["Economics", "Statistics", "Research", "Writing"],
        "pathways": [
            "After Class 10: compare streams that keep Mathematics and Economics available, if offered.",
            "After Class 12: investigate eligible Economics, Statistics, Mathematics or policy-related degrees.",
            "Build data analysis, research and writing skills; some roles require postgraduate study."
        ],
        "subjects": ["Economics", "Mathematics", "Statistics", "English"],
        "source_verified": False,
    },
    {
        "title": "Marketing Specialist", "sector": "Marketing and Media",
        "description": "Researches audiences and helps communicate the value of products, services or causes.",
        "interests": ["business", "creativity", "communication", "research"],
        "skills": ["Writing", "Audience research", "Analytics", "Creativity"],
        "pathways": [
            "After Class 10: explore any stream that suits your strengths and future study goals.",
            "After Class 12: compare eligible degrees in marketing, business, media, communications or related fields.",
            "Build writing samples, research projects and ethical digital marketing skills."
        ],
        "subjects": ["Business Studies", "Economics", "English", "Computer Applications"],
        "source_verified": False,
    },
    {
        "title": "Graphic Designer", "sector": "Design and Media",
        "description": "Creates visual communication for digital products, brands, publications and campaigns.",
        "interests": ["creativity", "visual_design", "technology", "communication"],
        "skills": ["Visual design", "Typography", "Creative software", "Portfolio development"],
        "pathways": [
            "After Class 10: explore arts, design, computer applications or vocational options available locally.",
            "After Class 12: research design degrees, diplomas and institution-specific entrance or portfolio requirements.",
            "Build a portfolio of original work and practise design fundamentals."
        ],
        "subjects": ["Art", "Design", "Computer Applications"],
        "source_verified": False,
    },
    {
        "title": "Architect", "sector": "Architecture and Built Environment",
        "description": "Plans building spaces and works with clients and technical teams on the built environment.",
        "interests": ["creativity", "mathematics", "building", "visual_design"],
        "skills": ["Design", "Spatial reasoning", "Drawing", "Communication"],
        "pathways": [
            "After Class 10: research the subject combinations required by architecture programs you may target.",
            "After Class 12: check current Council of Architecture rules, accepted entrance routes and institution requirements.",
            "Build drawing, design and spatial problem-solving skills."
        ],
        "subjects": ["Mathematics", "Art", "Design", "Physics"],
        "source_verified": False,
    },
    {
        "title": "Civil Engineer", "sector": "Engineering",
        "description": "Plans, designs and helps build infrastructure such as roads, buildings and water systems.",
        "interests": ["mathematics", "science", "building", "problem_solving"],
        "skills": ["Mathematics", "Physics", "Design", "Project coordination"],
        "pathways": [
            "After Class 10: compare a Science-with-Mathematics route and recognised diploma options.",
            "After Class 12 or diploma: verify the eligibility and admission route for the engineering program.",
            "Develop physics, mathematics, design and teamwork skills."
        ],
        "subjects": ["Mathematics", "Physics", "Chemistry"],
        "source_verified": False,
    },
    {
        "title": "Electrical / Electronics Engineer", "sector": "Engineering",
        "description": "Designs, tests and maintains electrical systems, circuits and electronic equipment.",
        "interests": ["mathematics", "technology", "building", "problem_solving"],
        "skills": ["Physics", "Circuit design", "Mathematics", "Testing"],
        "pathways": [
            "After Class 10: explore Science with Mathematics or relevant polytechnic diploma options.",
            "After Class 12 or diploma: research eligible electrical, electronics or related engineering programs.",
            "Practise safe electronics projects and learn circuit fundamentals."
        ],
        "subjects": ["Mathematics", "Physics", "Computer Science"],
        "source_verified": False,
    },
    {
        "title": "Mechanical Engineer", "sector": "Engineering",
        "description": "Designs and improves machines, mechanical systems and manufacturing processes.",
        "interests": ["mathematics", "building", "science", "problem_solving"],
        "skills": ["Physics", "CAD", "Design", "Manufacturing basics"],
        "pathways": [
            "After Class 10: compare Science with Mathematics and mechanical/related diploma routes.",
            "After Class 12 or diploma: verify eligibility for recognised mechanical engineering programs.",
            "Explore safe design projects, CAD and mechanics."
        ],
        "subjects": ["Mathematics", "Physics", "Chemistry"],
        "source_verified": False,
    },
    {
        "title": "Environmental Scientist", "sector": "Environment",
        "description": "Studies ecosystems, pollution and environmental change to inform conservation and policy.",
        "interests": ["biology", "research", "science", "helping_people"],
        "skills": ["Field observation", "Data analysis", "Biology", "Research writing"],
        "pathways": [
            "After Class 10: compare science combinations that support biology, chemistry or geography interests.",
            "After Class 12: explore eligible environmental science, ecology, geography or related degrees.",
            "Build research and data skills through supervised projects."
        ],
        "subjects": ["Biology", "Chemistry", "Geography", "Mathematics"],
        "source_verified": False,
    },
    {
        "title": "Agricultural Scientist", "sector": "Agriculture",
        "description": "Researches crops, soil, farming systems and technology to improve agricultural outcomes.",
        "interests": ["biology", "research", "building", "problem_solving"],
        "skills": ["Biology", "Chemistry", "Data collection", "Research"],
        "pathways": [
            "After Class 10: investigate science and agriculture-related options in your state.",
            "After Class 12: check current eligibility for agricultural universities and relevant degrees.",
            "Explore supervised gardening, soil, plant or agricultural data projects."
        ],
        "subjects": ["Biology", "Chemistry", "Mathematics", "Agriculture"],
        "source_verified": False,
    },
    {
        "title": "Psychologist", "sector": "Psychology and Social Sciences",
        "description": "Studies behaviour and mental processes; professional practice requirements depend on the role.",
        "interests": ["helping_people", "research", "communication", "problem_solving"],
        "skills": ["Research methods", "Listening", "Ethics", "Writing"],
        "pathways": [
            "After Class 10: explore streams that fit your interests; Psychology may be offered at different stages by different boards.",
            "After Class 12: investigate Psychology degrees and the qualifications required for your intended role.",
            "Check applicable professional regulations before planning clinical practice."
        ],
        "subjects": ["Psychology", "Biology", "Statistics", "English"],
        "source_verified": False,
    },
    {
        "title": "Lawyer", "sector": "Law and Public Service",
        "description": "Researches legal issues, advises clients or represents parties within the legal system.",
        "interests": ["communication", "research", "problem_solving", "detail"],
        "skills": ["Reading", "Writing", "Reasoning", "Ethics"],
        "pathways": [
            "After Class 10: Humanities, Commerce and Science may all be worth comparing based on your interests.",
            "After Class 12: investigate recognised integrated law degrees and current entrance requirements.",
            "Build reading, writing, debate and critical-reasoning skills."
        ],
        "subjects": ["English", "Political Science", "History", "Economics"],
        "source_verified": False,
    },
    {
        "title": "Journalist / Reporter", "sector": "Media and Communication",
        "description": "Researches, verifies and communicates news and stories to the public.",
        "interests": ["communication", "research", "creativity", "helping_people"],
        "skills": ["Writing", "Interviewing", "Fact-checking", "Digital media"],
        "pathways": [
            "After Class 10: explore subjects that strengthen language, society and media interests.",
            "After Class 12: compare journalism, media studies, communications and related qualifications.",
            "Practise ethical reporting, fact-checking and clear writing."
        ],
        "subjects": ["English", "History", "Political Science", "Media Studies"],
        "source_verified": False,
    },
    {
        "title": "Teacher / Educator", "sector": "Education",
        "description": "Supports learning and student development in a subject or age group.",
        "interests": ["helping_people", "communication", "research", "creativity"],
        "skills": ["Subject knowledge", "Communication", "Planning", "Empathy"],
        "pathways": [
            "After Class 10: identify subjects or age groups you may enjoy teaching.",
            "After Class 12: research relevant degrees and approved teacher-education qualifications.",
            "Verify current teacher eligibility and recruitment rules for your intended school system."
        ],
        "subjects": ["Relevant subject area", "English", "Psychology"],
        "source_verified": False,
    },
    {
        "title": "Police / Public Service Careers", "sector": "Public Service",
        "description": "Public-service roles vary widely and have specific education, age, fitness and recruitment requirements.",
        "interests": ["helping_people", "communication", "problem_solving", "leadership"],
        "skills": ["Communication", "Civic knowledge", "Fitness where required", "Integrity"],
        "pathways": [
            "After Class 10: check state-specific entry-level vocational and recruitment rules.",
            "For officer and civil-service routes, research required qualifications and official recruitment notices.",
            "Never rely on coaching advertisements alone; verify age, qualification and exam requirements with official recruiters."
        ],
        "subjects": ["Civics", "Political Science", "History", "English"],
        "source_verified": False,
    },
    {
        "title": "Hotel and Hospitality Manager", "sector": "Hospitality and Tourism",
        "description": "Coordinates guest services, hotel operations, food service or travel experiences.",
        "interests": ["helping_people", "communication", "business", "leadership"],
        "skills": ["Customer service", "Planning", "Communication", "Operations"],
        "pathways": [
            "After Class 10: explore recognised vocational and hospitality options available locally.",
            "After Class 12: compare approved hospitality degrees, diplomas and current admission criteria.",
            "Develop language, teamwork, customer service and practical experience."
        ],
        "subjects": ["English", "Business Studies", "Home Science", "Vocational Hospitality"],
        "source_verified": False,
    },
    {
        "title": "Chef / Culinary Professional", "sector": "Food and Hospitality",
        "description": "Plans and prepares food while following safety, quality and kitchen operations standards.",
        "interests": ["creativity", "building", "detail", "business"],
        "skills": ["Food safety", "Cooking techniques", "Planning", "Teamwork"],
        "pathways": [
            "After Class 10: investigate recognised culinary and vocational training options.",
            "After Class 10 or 12 depending on course: check entry rules for culinary diplomas and hospitality programs.",
            "Build safe practical skills and verify institute recognition and placement claims."
        ],
        "subjects": ["Vocational Hospitality", "Home Science", "Business Studies"],
        "source_verified": False,
    },
    {
        "title": "Fashion Designer", "sector": "Fashion and Design",
        "description": "Develops clothing, accessories or textile concepts and takes designs toward production.",
        "interests": ["creativity", "visual_design", "business", "building"],
        "skills": ["Drawing", "Textiles", "Design software", "Portfolio development"],
        "pathways": [
            "After Class 10: explore art, textiles, design and vocational opportunities.",
            "After Class 12: research fashion design degrees/diplomas and institution-specific selection requirements.",
            "Create an original portfolio and learn materials, sustainability and production basics."
        ],
        "subjects": ["Art", "Design", "Textiles", "Business Studies"],
        "source_verified": False,
    },
    {
        "title": "Animation / VFX Artist", "sector": "Creative Technology",
        "description": "Creates animated visuals, effects and digital assets for films, games and online media.",
        "interests": ["creativity", "visual_design", "technology", "building"],
        "skills": ["Drawing", "3D tools", "Storytelling", "Visual problem-solving"],
        "pathways": [
            "After Class 10: explore art, design, computer applications and vocational options.",
            "After Class 12: compare animation, multimedia and design programs; check entry requirements.",
            "Build a portfolio and learn fundamentals before purchasing expensive courses."
        ],
        "subjects": ["Art", "Computer Applications", "Design"],
        "source_verified": False,
    },
    {
        "title": "Game Developer", "sector": "Gaming and Technology",
        "description": "Builds game systems, gameplay logic and interactive experiences.",
        "interests": ["technology", "creativity", "problem_solving", "building"],
        "skills": ["Programming", "Game design", "Mathematics", "Teamwork"],
        "pathways": [
            "After Class 10: explore Mathematics, computing and design options available at your school.",
            "After Class 12: investigate eligible computing, game design or interactive media programs.",
            "Make small original games and learn coding, design and collaboration."
        ],
        "subjects": ["Mathematics", "Computer Science", "Art", "Design"],
        "source_verified": False,
    },
    {
        "title": "UX / UI Designer", "sector": "Product Design",
        "description": "Designs digital products that are understandable, accessible and useful for people.",
        "interests": ["creativity", "visual_design", "technology", "helping_people"],
        "skills": ["User research", "Prototyping", "Accessibility", "Communication"],
        "pathways": [
            "After Class 10: explore design, art, computing and communication interests.",
            "After Class 12: research eligible design, HCI, product design or computing programs.",
            "Build accessible prototypes and practise user research with consent."
        ],
        "subjects": ["Art", "Design", "Computer Applications", "Psychology"],
        "source_verified": False,
    },
    {
        "title": "Civil Services Officer", "sector": "Government and Policy",
        "description": "Works in public administration through specific competitive recruitment pathways.",
        "interests": ["helping_people", "research", "communication", "leadership"],
        "skills": ["Reading", "Writing", "Analysis", "Civic knowledge"],
        "pathways": [
            "After Class 10: choose subjects that support broad learning and current affairs.",
            "Complete a recognised undergraduate qualification that meets the relevant exam's current rules.",
            "Check official UPSC or state public service commission notices for eligibility and exam details."
        ],
        "subjects": ["History", "Political Science", "Economics", "Geography"],
        "source_verified": False,
    },
    {
        "title": "Research Scientist", "sector": "Science and Research",
        "description": "Investigates questions through experiments, modelling, observation or data analysis.",
        "interests": ["research", "mathematics", "biology", "problem_solving"],
        "skills": ["Scientific method", "Data analysis", "Writing", "Critical thinking"],
        "pathways": [
            "After Class 10: explore the Science subjects related to your interests.",
            "After Class 12: compare relevant B.Sc, integrated science or engineering programs.",
            "Many research careers require postgraduate study; check requirements in the chosen field."
        ],
        "subjects": ["Physics", "Chemistry", "Biology", "Mathematics"],
        "source_verified": False,
    },
    {
        "title": "Statistician", "sector": "Data and Mathematics",
        "description": "Uses statistical methods to design studies, analyse data and communicate uncertainty.",
        "interests": ["mathematics", "research", "problem_solving", "detail"],
        "skills": ["Probability", "Statistics", "Programming", "Communication"],
        "pathways": [
            "After Class 10: prioritise building strong mathematics foundations if this field interests you.",
            "After Class 12: investigate eligible Statistics, Mathematics, Data Science or Economics degrees.",
            "Learn data visualisation, coding and responsible interpretation of evidence."
        ],
        "subjects": ["Mathematics", "Statistics", "Computer Science"],
        "source_verified": False,
    },
    {
        "title": "Actuary", "sector": "Insurance and Risk",
        "description": "Uses mathematics, statistics and financial theory to analyse risk and uncertainty.",
        "interests": ["mathematics", "problem_solving", "business", "detail"],
        "skills": ["Probability", "Statistics", "Finance", "Analytical writing"],
        "pathways": [
            "After Class 10: strengthen mathematics and problem-solving.",
            "After Class 12: check current eligibility and examination routes with the Institute of Actuaries of India.",
            "Plan for a series of professional exams and relevant practical experience."
        ],
        "subjects": ["Mathematics", "Statistics", "Economics", "Computer Science"],
        "source_verified": False,
    },
    {
        "title": "Supply Chain / Logistics Analyst", "sector": "Operations",
        "description": "Helps plan inventory, transport, procurement and the flow of goods or services.",
        "interests": ["business", "mathematics", "problem_solving", "detail"],
        "skills": ["Planning", "Spreadsheets", "Data analysis", "Communication"],
        "pathways": [
            "After Class 10: explore streams that fit your interests in business, technology or operations.",
            "After Class 12: compare eligible business, logistics, commerce, engineering or analytics programs.",
            "Learn spreadsheet modelling, process mapping and data analysis."
        ],
        "subjects": ["Mathematics", "Business Studies", "Economics", "Computer Applications"],
        "source_verified": False,
    },
    {
        "title": "Electrician", "sector": "Skilled Trades",
        "description": "Installs, maintains and repairs electrical systems following safety standards.",
        "interests": ["building", "technology", "problem_solving", "detail"],
        "skills": ["Electrical safety", "Practical troubleshooting", "Reading diagrams", "Precision"],
        "pathways": [
            "After Class 10: research recognised ITI electrician or other approved vocational training options.",
            "Check the exact entry requirements, course recognition, apprenticeship opportunities and local licensing rules.",
            "Prioritise supervised training and electrical safety; do not practise hazardous work unsupervised."
        ],
        "subjects": ["Mathematics", "Science", "Vocational Electrical"],
        "source_verified": False,
    },
    {
        "title": "Automotive Technician", "sector": "Skilled Trades and Mobility",
        "description": "Inspects, services and repairs vehicles and their mechanical or electronic systems.",
        "interests": ["building", "technology", "problem_solving", "detail"],
        "skills": ["Diagnostics", "Mechanical basics", "Electronics", "Safety"],
        "pathways": [
            "After Class 10: compare recognised ITI and automotive vocational programs.",
            "Check current course entry criteria, apprenticeship options and qualification recognition.",
            "Learn through supervised practical training and follow workshop safety rules."
        ],
        "subjects": ["Mathematics", "Science", "Vocational Automotive"],
        "source_verified": False,
    },
    {
        "title": "Solar Energy Technician", "sector": "Renewable Energy",
        "description": "Supports installation, maintenance and troubleshooting of solar energy systems.",
        "interests": ["technology", "building", "science", "problem_solving"],
        "skills": ["Electrical basics", "Safety", "Troubleshooting", "Practical measurement"],
        "pathways": [
            "After Class 10: investigate approved electrical, renewable-energy and polytechnic training options.",
            "Check the current recognition and eligibility of each vocational or diploma course.",
            "Work under trained supervision and follow electrical and rooftop safety standards."
        ],
        "subjects": ["Mathematics", "Science", "Vocational Electrical"],
        "source_verified": False,
    },
    {
        "title": "Digital Marketing Specialist", "sector": "Digital Business",
        "description": "Plans and evaluates online campaigns, content and audience engagement.",
        "interests": ["business", "creativity", "communication", "technology"],
        "skills": ["Writing", "Analytics", "Audience research", "Ethical marketing"],
        "pathways": [
            "After Class 10: explore business, media, computing and communication interests.",
            "After Class 12: compare eligible marketing, business, communications or media qualifications.",
            "Practise with small projects and learn privacy, consent and advertising standards."
        ],
        "subjects": ["Business Studies", "English", "Computer Applications", "Economics"],
        "source_verified": False,
    },
    {
        "title": "Content Writer / Editor", "sector": "Writing and Communication",
        "description": "Creates, edits and verifies written material for audiences and organisations.",
        "interests": ["creativity", "communication", "research", "detail"],
        "skills": ["Writing", "Editing", "Research", "Fact-checking"],
        "pathways": [
            "After Class 10: develop language, reading and research skills across subjects.",
            "After Class 12: explore eligible humanities, journalism, language, media or domain-specific degrees.",
            "Build a portfolio and practise accurate sourcing and responsible AI use."
        ],
        "subjects": ["English", "Languages", "History", "Media Studies"],
        "source_verified": False,
    },
    {
        "title": "Social Worker", "sector": "Community and Social Impact",
        "description": "Works with individuals, families and communities to connect people with support and services.",
        "interests": ["helping_people", "communication", "research", "leadership"],
        "skills": ["Listening", "Ethics", "Community research", "Communication"],
        "pathways": [
            "After Class 10: explore Humanities, social sciences and community-service interests.",
            "After Class 12: research recognised social work, sociology, psychology or related degrees.",
            "Learn safeguarding, confidentiality and ethical community engagement."
        ],
        "subjects": ["Sociology", "Psychology", "Political Science", "English"],
        "source_verified": False,
    },
    {
        "title": "Tourism / Travel Consultant", "sector": "Travel and Tourism",
        "description": "Helps people plan travel, understand destinations and coordinate travel services.",
        "interests": ["communication", "business", "helping_people", "research"],
        "skills": ["Planning", "Customer service", "Languages", "Digital tools"],
        "pathways": [
            "After Class 10: explore recognised vocational tourism and hospitality courses.",
            "After Class 12: compare eligible tourism, travel, hospitality and business qualifications.",
            "Develop language skills, service skills and accurate destination research."
        ],
        "subjects": ["Geography", "English", "Business Studies", "Languages"],
        "source_verified": False,
    },
    {
        "title": "Interior Designer", "sector": "Design and Built Environment",
        "description": "Plans functional, safe and visually coherent interior spaces.",
        "interests": ["creativity", "visual_design", "building", "problem_solving"],
        "skills": ["Spatial planning", "Drawing", "Materials", "Communication"],
        "pathways": [
            "After Class 10: explore art, design, technical drawing and vocational options.",
            "After Class 12: research recognised interior design programs and entry requirements.",
            "Build a portfolio and learn accessibility, materials and safety basics."
        ],
        "subjects": ["Art", "Design", "Mathematics", "Computer Applications"],
        "source_verified": False,
    },
    {
        "title": "Product Designer", "sector": "Design and Innovation",
        "description": "Develops and improves physical or digital products based on user needs and constraints.",
        "interests": ["creativity", "building", "problem_solving", "visual_design"],
        "skills": ["Research", "Prototyping", "Design thinking", "Communication"],
        "pathways": [
            "After Class 10: explore science, art, design and practical making.",
            "After Class 12: compare eligible industrial, product, interaction or engineering design programs.",
            "Build prototypes, test with users ethically and document design decisions."
        ],
        "subjects": ["Art", "Design", "Mathematics", "Computer Science"],
        "source_verified": False,
    },
    {
        "title": "Biotechnologist", "sector": "Biotechnology",
        "description": "Applies biological science and technology in research, agriculture, healthcare or industry.",
        "interests": ["biology", "research", "chemistry", "problem_solving"],
        "skills": ["Biology", "Chemistry", "Lab safety", "Data analysis"],
        "pathways": [
            "After Class 10: explore relevant Science subject combinations.",
            "After Class 12: investigate eligible Biotechnology, Life Sciences or related qualifications.",
            "Follow laboratory safety rules; research roles may require postgraduate study."
        ],
        "subjects": ["Biology", "Chemistry", "Mathematics", "Physics"],
        "source_verified": False,
    },
    {
        "title": "Microbiologist", "sector": "Life Sciences",
        "description": "Studies microorganisms in health, food, environment, agriculture or research settings.",
        "interests": ["biology", "research", "chemistry", "detail"],
        "skills": ["Lab methods", "Biology", "Data recording", "Safety"],
        "pathways": [
            "After Class 10: build science foundations and explore Biology-related subjects.",
            "After Class 12: research eligible Microbiology, Biotechnology or Life Science degrees.",
            "Many specialised laboratory roles require further study and supervised training."
        ],
        "subjects": ["Biology", "Chemistry", "Physics"],
        "source_verified": False,
    },
    {
        "title": "Food Technologist", "sector": "Food Science",
        "description": "Works on food safety, processing, quality, product development and food systems.",
        "interests": ["science", "chemistry", "research", "detail"],
        "skills": ["Chemistry", "Food safety", "Quality control", "Data recording"],
        "pathways": [
            "After Class 10: compare Science and vocational food-processing options.",
            "After Class 12: research eligible Food Technology, Food Science or related programs.",
            "Check course recognition, laboratory requirements and industry safety standards."
        ],
        "subjects": ["Chemistry", "Biology", "Mathematics", "Physics"],
        "source_verified": False,
    },
    {
        "title": "Geologist", "sector": "Earth and Environmental Science",
        "description": "Studies Earth's materials, structure, resources and processes.",
        "interests": ["research", "science", "building", "problem_solving"],
        "skills": ["Geology", "Field observation", "Data analysis", "Mapping"],
        "pathways": [
            "After Class 10: explore Science and Geography interests.",
            "After Class 12: research eligible Geology, Earth Science or related degrees and subject requirements.",
            "Build field observation, mapping and data interpretation skills."
        ],
        "subjects": ["Geology", "Geography", "Chemistry", "Mathematics"],
        "source_verified": False,
    },
    {
        "title": "Urban Planner", "sector": "Cities and Public Policy",
        "description": "Helps plan land use, transport, housing and public spaces in towns and cities.",
        "interests": ["building", "research", "helping_people", "problem_solving"],
        "skills": ["Geography", "Data analysis", "Design", "Public communication"],
        "pathways": [
            "After Class 10: explore geography, mathematics, civics and design interests.",
            "After Class 12: research eligible planning, geography, architecture or related qualifications.",
            "Learn about accessibility, sustainability and community participation."
        ],
        "subjects": ["Geography", "Mathematics", "Economics", "Civics"],
        "source_verified": False,
    },
    {
        "title": "Librarian / Information Specialist", "sector": "Information and Knowledge",
        "description": "Organises information resources and helps people find, evaluate and use information.",
        "interests": ["research", "communication", "detail", "helping_people"],
        "skills": ["Organisation", "Research", "Digital literacy", "Communication"],
        "pathways": [
            "After Class 10: develop reading, information and digital skills.",
            "After Class 12: research library science and information management qualifications and entry rules.",
            "Check the qualification required for the specific role and institution."
        ],
        "subjects": ["English", "Languages", "Computer Applications"],
        "source_verified": False,
    },
    {
        "title": "Financial Analyst", "sector": "Finance",
        "description": "Analyses financial information to support business, investment or budgeting decisions.",
        "interests": ["mathematics", "business", "research", "detail"],
        "skills": ["Accounting", "Excel", "Statistics", "Communication"],
        "pathways": [
            "After Class 10: explore Commerce, Mathematics and Economics options.",
            "After Class 12: compare eligible Finance, Economics, Accounting, Commerce or Statistics degrees.",
            "Learn financial literacy, spreadsheets and ethical analysis; do not treat this as investment advice."
        ],
        "subjects": ["Mathematics", "Economics", "Accountancy", "Business Studies"],
        "source_verified": False,
    },
    {
        "title": "Banking Professional", "sector": "Banking and Finance",
        "description": "Supports banking operations, customer service, credit, compliance or financial services.",
        "interests": ["business", "mathematics", "communication", "detail"],
        "skills": ["Numeracy", "Customer service", "Compliance", "Data handling"],
        "pathways": [
            "After Class 10: explore Commerce, Mathematics and communication skills.",
            "For many officer-level roles, complete a qualifying degree and check the current recruitment notice.",
            "Verify each bank's official eligibility, examination and age criteria."
        ],
        "subjects": ["Mathematics", "Economics", "Accountancy", "English"],
        "source_verified": False,
    },
    {
        "title": "Flight / Aviation Professional", "sector": "Aviation",
        "description": "Aviation includes pilots, aircraft maintenance, air traffic, cabin crew and airport operations, each with different rules.",
        "interests": ["technology", "problem_solving", "communication", "detail"],
        "skills": ["Safety", "Communication", "Technical knowledge", "Decision-making"],
        "pathways": [
            "After Class 10: compare aviation and technical routes carefully; requirements vary greatly by role.",
            "For pilot or licensed technical roles, check current DGCA requirements, medical criteria and approved training providers.",
            "Verify total cost, licensing, safety standards and training approval before enrolling."
        ],
        "subjects": ["Mathematics", "Physics", "English", "Computer Science"],
        "source_verified": False,
    },
    {
        "title": "Air Traffic / Airport Operations", "sector": "Aviation Operations",
        "description": "Supports safe and efficient movement of aircraft or airport services through specialist operational roles.",
        "interests": ["problem_solving", "communication", "detail", "technology"],
        "skills": ["Situational awareness", "Communication", "Safety procedures", "Teamwork"],
        "pathways": [
            "After Class 10: explore relevant Science and communication subjects.",
            "Check the current official eligibility and recruitment route for the specific airport or air-traffic role.",
            "Treat medical, age, licensing and examination requirements as role-specific."
        ],
        "subjects": ["Mathematics", "Physics", "English"],
        "source_verified": False,
    },
    {
        "title": "Sports Coach / Fitness Professional", "sector": "Sports and Wellness",
        "description": "Supports athletic skill, physical training and fitness using appropriate training and safety principles.",
        "interests": ["helping_people", "building", "communication", "leadership"],
        "skills": ["Training principles", "Communication", "Safety", "Planning"],
        "pathways": [
            "After Class 10: continue sports safely and explore recognised sports or vocational education options.",
            "After Class 12: research approved sports science, physical education or coaching qualifications.",
            "Check certification requirements for the specific role; avoid unsafe training practices."
        ],
        "subjects": ["Physical Education", "Biology", "Psychology"],
        "source_verified": False,
    },
    {
        "title": "Nutrition / Dietetics Professional", "sector": "Nutrition and Wellness",
        "description": "Studies food and nutrition; professional scope depends on qualification, role and applicable rules.",
        "interests": ["biology", "helping_people", "research", "detail"],
        "skills": ["Nutrition science", "Communication", "Research", "Ethics"],
        "pathways": [
            "After Class 10: explore Biology and food science interests.",
            "After Class 12: research eligible Nutrition, Dietetics or Food Science qualifications.",
            "Check professional requirements for the role; do not provide medical nutrition care without appropriate qualifications."
        ],
        "subjects": ["Biology", "Chemistry", "Home Science"],
        "source_verified": False,
    },
]

class Command(BaseCommand):
    help = "Insert or update illustrative career catalogue entries."

    def handle(self, *args, **options):
        for item in SEED:
            Career.objects.update_or_create(title=item["title"], defaults=item)
        self.stdout.write(self.style.SUCCESS(
            f"Seeded/updated {len(SEED)} illustrative careers. Verify official requirements before production."
        ))
