import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import PrivateRoute from './utils/privateRoute.util.js'
import { AuthProvider } from './context/authentication.context.js';

import LoginPage from './pages/login.page.js'
import HomePage from './pages/home.page.js';
import AccountPage from './pages/account.page.js';

function App() {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route path='/login' element={ <LoginPage/> } />
          <Route 
            path='/'
            element={
              <PrivateRoute>
                <HomePage />
              </PrivateRoute>
            }
          />
          <Route 
            path='/account'
            element={
              <PrivateRoute>
                <AccountPage />
              </PrivateRoute>
            }
          />
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;
