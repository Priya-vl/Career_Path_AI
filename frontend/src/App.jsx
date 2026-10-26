import { useEffect, useMemo, useState } from 'react'
import { Link, NavLink, Route, Routes, useNavigate } from 'react-router-dom'
import { ArrowRight, BookOpen, Brain, Compass, GraduationCap, LogIn, LogOut, MessageCircle, Search, ShieldCheck, Sparkles, Users, GitBranch, Sprout, HeartPulse, Landmark, Palette, Wrench, ChevronRight, CheckCircle2, Map, Target } from 'lucide-react'
import { api, getAccess, logout, setTokens } from './api'

const sampleInterests = [
  ['technology','Technology'], ['problem_solving','Problem-solving'], ['mathematics','Mathematics'],
  ['biology','Biology and health'], ['helping_people','Helping people'], ['business','Business'],
  ['creativity','Creativity'], ['visual_design','Visual design'], ['research','Research'],
  ['building','Building things'], ['communication','Communication'], ['detail','Attention to detail']
]

function Header({ user, onLogout }) {
  return <header className="header"><Link className="brand" to="/"><span className="brand-mark"><Compass size={22}/></span><span>CareerPath <b>AI</b></span></Link>
    <nav><NavLink to="/">Home</NavLink><NavLink to="/assessment">Assessment</NavLink><NavLink to="/mindmap">Career map</NavLink><NavLink to="/explore">Explore careers</NavLink></nav>
    <div className="header-actions">{user ? <><span className="user-chip">{user.first_name || user.username}</span><button className="icon-button" onClick={onLogout} title="Log out"><LogOut size={18}/></button></> : <Link className="button button-small" to="/login"><LogIn size={16}/> Sign in</Link>}</div>
  </header>
}

function Home() {
  return <><section className="hero"><div className="hero-copy"><div className="eyebrow"><Sparkles size={15}/> YOUR FUTURE, EXPLORED</div><h1>Big dreams start with <span>better choices.</span></h1><p className="hero-text">Understand your interests. Explore what to study after Class 10. Discover college pathways and careers that could fit you.</p><div className="hero-buttons"><Link className="button" to="/assessment">Discover my interests <ArrowRight size={18}/></Link><Link className="button button-ghost" to="/explore">Explore careers</Link></div><div className="hero-note"><ShieldCheck size={17}/> Explore possibilities — your future is yours to choose.</div></div>
    <div className="hero-visual"><div className="orbit orbit-one"></div><div className="orbit orbit-two"></div><div className="hero-center"><GraduationCap size={52}/><b>Your path</b><span>Starts here</span></div><div className="float-card card-one"><Brain size={20}/><div><b>Know yourself</b><small>Explore interests</small></div></div><div className="float-card card-two"><BookOpen size={20}/><div><b>Explore options</b><small>Courses & streams</small></div></div><div className="float-card card-three"><Sparkles size={20}/><div><b>Build a roadmap</b><small>One step at a time</small></div></div></div></section>
    <section className="section"><div className="section-heading"><div className="eyebrow">A CLEARER WAY FORWARD</div><h2>From school to a career, one step at a time</h2><p>Learn what each choice can open up — and compare more than one path.</p></div><div className="feature-grid">
      <Feature icon={<Brain/>} number="01" title="Discover your interests" text="Answer simple questions about subjects, activities and what you enjoy."/>
      <Feature icon={<BookOpen/>} number="02" title="Understand your options" text="Explore Science, Commerce, Humanities, diploma and vocational pathways."/>
      <Feature icon={<Compass/>} number="03" title="Map your next steps" text="Connect school subjects to qualifications, skills and possible careers."/>
    </div></section>
    <section className="callout"><div><div className="eyebrow">NO SINGLE RIGHT PATH</div><h2>Your interests are a starting point, not a limit.</h2><p>Compare different routes, ask questions and talk through your choices with a trusted adult or counsellor.</p></div><Link className="button" to="/assessment">Start exploring <ArrowRight size={18}/></Link></section>
    <footer><span>CareerPath AI</span><span>Guidance, not a guarantee. Verify admission requirements with official sources.</span></footer></>
}
function Feature({icon, number, title, text}) { return <article className="feature-card"><div className="feature-top"><span className="feature-icon">{icon}</span><span className="feature-number">{number}</span></div><h3>{title}</h3><p>{text}</p></article> }

function Login({ onLogin }) {
  const [mode, setMode] = useState('login')
  const [form, setForm] = useState({username:'', password:'', email:'', first_name:'', last_name:'', role:'student', current_class:'9', state:'Karnataka', board:'Karnataka State Board'})
  const [error, setError] = useState('')
  const [busy, setBusy] = useState(false)
  const nav = useNavigate()
  const update = (key, value) => setForm({...form, [key]: value})
  async function submit(e) {
    e.preventDefault(); setError(''); setBusy(true)
    try {
      if (mode === 'register') await api('/auth/register/', {method:'POST', body:JSON.stringify({...form, current_class:form.role === 'student' && form.current_class ? Number(form.current_class) : null})})
      const tokens = await api('/auth/token/', {method:'POST', body:JSON.stringify({username:form.username,password:form.password})})
      setTokens(tokens)
      const me = await api('/auth/me/')
      onLogin(me); nav('/')
    } catch(err) { setError(err.message) } finally { setBusy(false) }
  }
  return <main className="auth-page"><div className="auth-panel"><div className="auth-icon"><GraduationCap/></div><div className="eyebrow">WELCOME TO CAREERPATH AI</div><h1>{mode === 'login' ? 'Welcome back' : form.role === 'parent' ? 'Create a parent account' : 'Create your student account'}</h1><p>Explore education choices together. Your account helps save pathways and progress.</p>
    <form onSubmit={submit} className="form">
      {mode === 'register' && <><label>I am a<select value={form.role} onChange={e=>update('role',e.target.value)}><option value="student">Student</option><option value="parent">Parent / Guardian</option></select></label><div className="form-row"><label>First name<input value={form.first_name} onChange={e=>update('first_name',e.target.value)} /></label><label>Last name<input value={form.last_name} onChange={e=>update('last_name',e.target.value)} /></label></div><label>Email<input type="email" required value={form.email} onChange={e=>update('email',e.target.value)} /></label>{form.role === 'student' && <label>Current class<select value={form.current_class} onChange={e=>update('current_class',e.target.value)}>{[8,9,10,11,12].map(n=><option key={n} value={n}>Class {n}</option>)}</select></label>}<div className="form-row"><label>State<select value={form.state} onChange={e=>update('state',e.target.value)}><option>Karnataka</option><option>Tamil Nadu</option></select></label><label>Education board<select value={form.board} onChange={e=>update('board',e.target.value)}><option>Karnataka State Board</option><option>Tamil Nadu State Board</option><option>CBSE</option><option>ICSE</option><option>IGCSE</option></select></label></div></>}
      <label>Username<input required autoComplete="username" value={form.username} onChange={e=>update('username',e.target.value)} /></label><label>Password<input required type="password" minLength="8" autoComplete={mode==='login'?'current-password':'new-password'} value={form.password} onChange={e=>update('password',e.target.value)} /></label>
      {error && <div className="error">{error}</div>}<button className="button full" disabled={busy}>{busy ? 'Please wait…' : mode === 'login' ? 'Sign in' : 'Create account'} <ArrowRight size={17}/></button>
    </form><p className="auth-switch">{mode==='login'?'New to CareerPath AI?':'Already have an account?'} <button onClick={()=>{setMode(mode==='login'?'register':'login');setError('')}}>{mode==='login'?'Create account':'Sign in'}</button></p><p className="tiny">Prototype notice: do not enter real children's data until guardian-consent and production privacy controls are implemented.</p></div></main>
}

function Explore() {
  const [careers,setCareers] = useState([])
  const [query,setQuery] = useState('')
  const [error,setError] = useState('')
  useEffect(()=>{api('/careers/').then(setCareers).catch(e=>setError(e.message))},[])
  const filtered = useMemo(()=>careers.filter(c=>(c.title+' '+c.sector+' '+c.description).toLowerCase().includes(query.toLowerCase())),[careers,query])
  return <main className="page"><div className="page-heading"><div className="eyebrow">CAREER LIBRARY</div><h1>Explore what’s possible.</h1><p>Start with curiosity. Learn what different careers involve and what pathways you can research.</p></div><div className="search-box"><Search size={19}/><input value={query} onChange={e=>setQuery(e.target.value)} placeholder="Search careers, skills or sectors…"/></div>{error && <div className="error">{error}. Is the backend running?</div>}<div className="career-grid">{filtered.map(c=><article className="career-card" key={c.id}><div className="career-sector">{c.sector}</div><h3>{c.title}</h3><p>{c.description}</p><div className="tag-list">{(c.skills||[]).slice(0,3).map(s=><span className="tag" key={s}>{s}</span>)}</div><details><summary>Explore possible pathways</summary><ul>{(c.pathways||[]).map(p=><li key={p}>{p}</li>)}</ul><p className="source-warning">{c.source_verified?'Source marked verified':'Illustrative pathway — verify current official requirements.'}</p></details></article>)}</div>{!filtered.length&&!error&&<div className="empty">No careers match that search yet. Try another term.</div>}</main>
}

function Assessment({ user }) {
  const [selected,setSelected] = useState([])
  const [results,setResults] = useState(null)
  const [error,setError] = useState('')
  const [busy,setBusy] = useState(false)
  function toggle(key) { setSelected(prev=>prev.includes(key)?prev.filter(x=>x!==key):[...prev,key]) }
  async function submit(e) { e.preventDefault();setBusy(true);setError('');try{setResults(await api('/guidance/recommendations/',{method:'POST',body:JSON.stringify({interests:selected,current_class:user?.current_class,state:user?.state,board:user?.board})}))}catch(err){setError(err.message)}finally{setBusy(false)} }
  return <main className="page"><div className="page-heading"><div className="eyebrow">INTEREST ASSESSMENT</div><h1>What are you curious about?</h1><p>Select at least two areas you enjoy or want to explore. There are no right or wrong answers.</p></div>
    {!getAccess() && <div className="info-banner">Sign in first to save and submit your assessment. <Link to="/login">Sign in or register</Link></div>}
    <form className="assessment-panel" onSubmit={submit}><div className="assessment-meta"><span>YOUR INTERESTS</span><span>{selected.length} selected</span></div><div className="interest-grid">{sampleInterests.map(([key,label])=><button type="button" className={`interest-option ${selected.includes(key)?'selected':''}`} key={key} onClick={()=>toggle(key)}><span className="check">{selected.includes(key)?'✓':'+'}</span>{label}</button>)}</div>{error&&<div className="error">{error}</div>}<button className="button" disabled={!getAccess()||selected.length<2||busy}>{busy?'Finding possible matches…':'Explore my matches'} <ArrowRight size={18}/></button></form>
    {results&&<section className="results"><div className="eyebrow">YOUR EXPLORATION STARTING POINTS</div><h2>Career areas to explore</h2><p>{results.notice}</p><div className="career-grid">{results.results.map(r=><article className="career-card result-card" key={r.career.id}><div className="match-line"><span className="career-sector">{r.career.sector}</span><strong>{r.match_score}% interest overlap</strong></div><h3>{r.career.title}</h3><p>{r.career.description}</p><p className="match-explain">{r.explanation}</p><Link to="/mindmap">Open your interactive career map →</Link></article>)}</div></section>}
  </main>
}

const pathwayMap = {
  'Science · Mathematics': {icon:Brain, desc:'For students curious about numbers, systems, technology and how things work.', courses:['Engineering','Computer Science','Architecture*','Statistics & Mathematics','Physics','Data Science'], careers:['AI / ML specialist','Civil engineer','Robotics technician','Geospatial analyst','Actuary','Renewable-energy engineer','Game developer','Semiconductor technician'], note:'*Some courses have specific subject and entrance requirements.'},
  'Science · Biology': {icon:HeartPulse, desc:'Explore living systems, health, food, animals and the environment.', courses:['Medicine & allied health','Biotechnology','Agriculture','Microbiology','Nutrition','Environmental science'], careers:['Doctor','Nurse','Medical laboratory technologist','Food scientist','Agricultural scientist','Wildlife conservationist','Genetic counsellor','Aquaculture specialist'], note:'Clinical and regulated careers may require specific recognised qualifications.'},
  'Commerce & Business': {icon:Landmark, desc:'Understand money, organisations, markets, people and how businesses operate.', courses:['Commerce','Economics','Accounting & Finance','Business Administration','Supply Chain','Hospitality'], careers:['Accountant','Forensic accountant','Actuary','Logistics planner','Market researcher','Tax professional','Entrepreneur','Procurement specialist'], note:'Mathematics requirements vary by course and institution.'},
  'Humanities & Society': {icon:Palette, desc:'Explore history, languages, people, culture, communication and public life.', courses:['History','Psychology','Law','Design','Journalism','Social Work','Public Policy'], careers:['Archaeologist','Archivist','UX researcher','Museum educator','Translator','Policy analyst','Heritage conservator','Accessibility specialist'], note:'Check the entry requirements for each course and professional route.'},
  'Vocational & Skilled Work': {icon:Wrench, desc:'Build practical skills through training, apprenticeships, certificates and hands-on experience.', courses:['ITI trades','Polytechnic diploma','Apprenticeship','Agriculture & horticulture','Electrical systems','Automotive technology'], careers:['Electrician','Solar PV technician','CNC operator','Drone service operator','Refrigeration technician','Welding specialist','Farm enterprise owner','Water-treatment operator'], note:'Trade availability and admission rules depend on the state, institution and qualification.'}
}
function CareerMindMap({user}) {
  const [stream,setStream] = useState('Science · Mathematics')
  const [expanded,setExpanded] = useState('courses')
  const [selectedCareer,setSelectedCareer] = useState('AI / ML specialist')
  const data = pathwayMap[stream]
  return <main className="page mindmap-page"><div className="page-heading"><div className="eyebrow"><GitBranch size={14}/> YOUR FUTURE, CONNECTED</div><h1>Your career universe.</h1><p>Start from a subject direction and explore the courses, specialisations and careers it may connect to. This is a discovery map—not a fixed prediction.</p></div>
    <div className="map-controls"><div><span className="mini-label">YOUR STARTING POINT</span><strong>{user?.current_class ? `Class ${user.current_class}` : 'Classes 8–10'}</strong><small>{user?.board || 'Choose your board in your profile'} · {user?.state || 'India'}</small></div><Link className="button button-small" to="/assessment"><Target size={16}/> Take assessment</Link></div>
    <div className="stream-tabs">{Object.entries(pathwayMap).map(([name,info])=>{const Icon=info.icon;return <button key={name} className={stream===name?'stream-tab active':'stream-tab'} onClick={()=>{setStream(name);setSelectedCareer(pathwayMap[name].careers[0])}}><Icon size={18}/><span>{name}</span></button>})}</div>
    <section className="map-canvas"><div className="map-root"><span className="node-kicker">POSSIBLE DIRECTION</span><h2>{stream}</h2><p>{data.desc}</p></div><div className="map-branches"><button className={`branch-card ${expanded==='courses'?'branch-active':''}`} onClick={()=>setExpanded(expanded==='courses'?'':'courses')}><BookOpen/><span><b>Explore courses</b><small>What could I study?</small></span><ChevronRight/></button><button className={`branch-card ${expanded==='careers'?'branch-active':''}`} onClick={()=>setExpanded(expanded==='careers'?'':'careers')}><Compass/><span><b>Discover careers</b><small>What could I become or do?</small></span><ChevronRight/></button><button className={`branch-card ${expanded==='routes'?'branch-active':''}`} onClick={()=>setExpanded(expanded==='routes'?'':'routes')}><Map/><span><b>Alternative routes</b><small>Degrees, diplomas, ITI, training</small></span><ChevronRight/></button></div>
    {expanded==='courses'&&<div className="map-detail"><div className="detail-heading"><div><span className="mini-label">COURSE EXPLORER</span><h3>Possible college directions</h3></div><span className="count-pill">{data.courses.length} examples</span></div><div className="map-chip-grid">{data.courses.map(c=><div className="map-chip" key={c}><CheckCircle2 size={16}/>{c}</div>)}</div></div>}
    {expanded==='careers'&&<div className="map-detail"><div className="detail-heading"><div><span className="mini-label">CAREER EXPLORER</span><h3>Popular and less-heard-of possibilities</h3></div><span className="count-pill">{data.careers.length} examples</span></div><div className="map-career-grid">{data.careers.map((c,i)=><button key={c} className={`map-career ${selectedCareer===c?'chosen':''}`} onClick={()=>setSelectedCareer(c)}><span className="career-number">{String(i+1).padStart(2,'0')}</span><span><b>{c}</b><small>{i>3?'A field worth discovering':'Explore role and entry routes'}</small></span><ChevronRight size={16}/></button>)}</div><div className="career-insight"><Sparkles size={18}/><div><b>{selectedCareer}</b><p>Next, CareerPath AI will connect this role to required subjects, courses, eligibility, entrance exams, training, work settings and verified opportunities. Requirements must be checked for the relevant board and admission year.</p></div></div></div>}
    {expanded==='routes'&&<div className="map-detail"><div className="detail-heading"><div><span className="mini-label">MORE THAN ONE WAY FORWARD</span><h3>Explore entry routes</h3></div></div><div className="route-grid">{[['University degree','For careers requiring deeper academic study or professional qualifications.'],['Diploma / Polytechnic','A practical route into technical and applied fields.'],['ITI / Trade training','Hands-on skills for technical and skilled occupations.'],['Apprenticeship / Certificate','Learn through supervised practice and targeted training.']].map(([title,desc])=><article className="route-card" key={title}><CheckCircle2 size={19}/><b>{title}</b><p>{desc}</p></article>)}</div><p className="source-warning">Not every route qualifies for every occupation. Confirm eligibility with official institutions and regulators.</p></div>}
    </section><div className="map-footnote"><ShieldCheck size={17}/><span>Pathways are examples for exploration, not eligibility guarantees. School subject combinations vary by board and school.</span></div>
  </main>
}

function Chat({ user }) {
  const [question,setQuestion] = useState('')
  const [messages,setMessages] = useState([{role:'assistant',text:'Hi! I can help you explore career options. Ask me about subjects after Class 10, courses or career areas. I will be clear when current eligibility information needs official verification.'}])
  const [busy,setBusy] = useState(false)
  const [error,setError] = useState('')
  async function send(e) { e.preventDefault(); if(!question.trim())return; const q=question.trim();setQuestion('');setError('');setMessages(m=>[...m,{role:'user',text:q}]);setBusy(true);try{const d=await api('/guidance/chat/',{method:'POST',body:JSON.stringify({question:q})});setMessages(m=>[...m,{role:'assistant',text:d.answer,citations:d.citations}])}catch(err){setError(err.message)}finally{setBusy(false)} }
  return <main className="page chat-page"><div className="page-heading"><div className="eyebrow">CAREERPATH AI GUIDE</div><h1>Questions are a great place to start.</h1><p>Ask about streams, subjects, qualifications or career paths.</p></div>{!getAccess()&&<div className="info-banner">Sign in to use the guidance assistant. <Link to="/login">Sign in</Link></div>}<section className="chat-panel"><div className="chat-top"><div className="chat-avatar"><Sparkles/></div><div><b>CareerPath Guide</b><span>Education exploration assistant · starter mode</span></div><span className="online-dot"/></div><div className="chat-messages">{messages.map((m,i)=><div className={`message ${m.role}`} key={i}><div className="message-avatar">{m.role==='assistant'?<Sparkles size={16}/>:<Users size={16}/>}</div><div className="bubble">{m.text}{m.citations?.length>0&&<div className="citations">Sources: {m.citations.join(', ')}</div>}</div></div>)}{busy&&<div className="message assistant"><div className="message-avatar"><Sparkles size={16}/></div><div className="bubble">Thinking…</div></div>}</div>{error&&<div className="error chat-error">{error}</div>}<form className="chat-form" onSubmit={send}><input disabled={!getAccess()||busy} value={question} onChange={e=>setQuestion(e.target.value)} placeholder="Ask a career question…"/><button className="button" disabled={!getAccess()||busy||!question.trim()} aria-label="Send question"><MessageCircle size={18}/><span>Send</span></button></form><p className="chat-disclaimer">Starter mode does not retrieve verified source documents yet. Confirm admission rules with official authorities.</p></section></main>
}

function Dashboard({ user }) {
  const isParent = user?.role === 'parent'
  return <main className="page dashboard-page"><div className="welcome-banner"><div><div className="eyebrow">{isParent?'PARENT SPACE':'YOUR DISCOVERY SPACE'}</div><h1>{isParent?'Support their future.':'Hello'+(user?.first_name?`, ${user.first_name}`:'')+'.'}</h1><p>{isParent?'Explore pathways with your child and help them compare choices without limiting their possibilities.':'Your future has more possibilities than you may have heard about. Let’s explore them.'}</p><div className="welcome-actions"><Link className="button" to="/mindmap"><GitBranch size={17}/> Explore career map</Link>{!isParent&&<Link className="button button-ghost" to="/assessment">Start assessment <ArrowRight size={16}/></Link>}</div></div><div className="welcome-art"><div className="welcome-art-orbit"><Compass size={42}/></div><span className="art-dot dot-a"/><span className="art-dot dot-b"/><span className="art-dot dot-c"/></div></div><div className="dashboard-section-title"><div><span className="eyebrow">YOUR NEXT STEPS</span><h2>{isParent?'Explore together':'Your journey starts here'}</h2></div><span className="progress-label">Keep exploring ✦</span></div><div className="dashboard-grid"><div className="dashboard-card"><div className="dash-icon"><Brain/></div><h3>{isParent?'Understand interests':'Discover your interests'}</h3><p>{isParent?'Learn how interests can open different educational possibilities.':'Answer thoughtful questions about activities, subjects and what you enjoy.'}</p><Link className="text-link" to={isParent?"/mindmap":"/assessment"}>{isParent?'Explore pathways together':'Start assessment'} →</Link></div><div className="dashboard-card"><div className="dash-icon"><GitBranch/></div><h3>Interactive career map</h3><p>Move from school subjects to courses, specialisations and careers—including options you may not know yet.</p><Link className="text-link" to="/mindmap">Open career map →</Link></div><div className="dashboard-card"><div className="dash-icon"><BookOpen/></div><h3>Explore opportunities</h3><p>Browse different occupations and learn which qualifications and entry routes to research.</p><Link className="text-link" to="/explore">Explore career library →</Link></div></div>{isParent&&<div className="info-banner"><Users size={19}/> Child profile linking and shared progress are the next account feature. Until linked, this account does not display private student assessment data.</div>}<div className="info-banner"><ShieldCheck size={19}/> Role: <b>{user?.role||'student'}</b>. Assessment results are guidance—not a fixed label or a guarantee of admission.</div></main>
}

export default function App() {
  const [user,setUser] = useState(null)
  const [loading,setLoading] = useState(!!getAccess())
  const nav = useNavigate()
  useEffect(()=>{if(getAccess())api('/auth/me/').then(setUser).catch(()=>logout()).finally(()=>setLoading(false));else setLoading(false)},[])
  function onLogout(){logout();setUser(null);nav('/')}
  if(loading) return <div className="loading">Loading CareerPath AI…</div>
  return <div className="app-shell"><Header user={user} onLogout={onLogout}/><Routes><Route path="/" element={user?<Dashboard user={user}/>:<Home/>}/><Route path="/login" element={<Login onLogin={setUser}/>}/><Route path="/explore" element={<Explore/>}/><Route path="/assessment" element={<Assessment user={user}/>}/><Route path="/mindmap" element={<CareerMindMap user={user}/>}/><Route path="*" element={<Home/>}/></Routes></div>
}
