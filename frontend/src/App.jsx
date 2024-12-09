import { HashRouter as Router, Routes, Route } from "react-router-dom";

import MainPage from "./pages/MainPage"
import LoginPage from "./pages/LoginPage"
import SignupPage from "./pages/SignupPage"

function App() {

  return (
    <Router>
      <Routes>
        <Route path="/" element={<MainPage/>}/>
        <Route path="/login" element={<LoginPage/>}/>
        <Route path="/signup" element={<SignupPage/>}/>
        {/* <Route path="/profile" element={<ProfilePage/>}/> */}
        {/* <Route path="/my-wishlist" element={<MyWishlistPage/>}/> */}
        {/* <Route path="/wishlist/:userId" */}
        {/* loader={({ params }) => { */}
          {/* return fetchTeam(params.userId); */}
        {/* }} */}
         {/* element={<WishlistPage/>}/> */}
        {/* <Route path="/make-wish" element={<MakewishPage/>}/> */}
      </Routes>
    </Router>
  )
}

export default App