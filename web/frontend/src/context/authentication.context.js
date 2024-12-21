import { createContext, useContext, useState } from 'react';
import { setCookie, getCookie, deleteCookie } from "../utils/cookies.util"

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(() => {
    if(getCookie("MSSV")) return true
    return false
  });
  const [MSSV, setMSSV] = useState(() => getCookie("MSSV"))
  const [currentTerm, setCurrentTerm] = useState(() => getCookie("currentTerm"))

  const login = (MSSV) => {
    setMSSV(MSSV)
    setCookie('MSSV', MSSV, 3)
    setIsAuthenticated(true)
  };
  const logout = () => {
    setMSSV(null)
    deleteCookie('MSSV')
    setIsAuthenticated(false);
  }
  const updateCurrentTerm = (updatedCurrentTerm) => {
    setCurrentTerm(updatedCurrentTerm)
    setCookie('currentTerm', updatedCurrentTerm, 3)
  }

  return (
    <AuthContext.Provider value={{ isAuthenticated, MSSV, currentTerm, updateCurrentTerm, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
