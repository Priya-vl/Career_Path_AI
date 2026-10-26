const API = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000/api'
export function getAccess() { return localStorage.getItem('careerpath_access') }
export function setTokens(data) {
  if (data.access) localStorage.setItem('careerpath_access', data.access)
  if (data.refresh) localStorage.setItem('careerpath_refresh', data.refresh)
}
export function logout() {
  localStorage.removeItem('careerpath_access')
  localStorage.removeItem('careerpath_refresh')
}
export async function api(path, options = {}) {
  const headers = { 'Content-Type': 'application/json', ...(options.headers || {}) }
  const token = getAccess()
  if (token) headers.Authorization = `Bearer ${token}`
  const response = await fetch(`${API}${path}`, { ...options, headers })
  const raw = await response.text()
  let data = {}
  try { data = raw ? JSON.parse(raw) : {} } catch { data = { detail: raw } }
  if (!response.ok) {
    const detail = data.detail || Object.values(data).flat().join(' ') || 'Request failed'
    throw new Error(typeof detail === 'string' ? detail : JSON.stringify(detail))
  }
  return data
}
