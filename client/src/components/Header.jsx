import React, { useContext } from "react";
import { Link } from "react-router-dom";
import AuthContext from "../context/AuthContext";

const Header = () => {
  let { user, logoutUser } = useContext(AuthContext);
  return (
    <div className="navbar">
      <Link to="/" className="btn-ghost btn">Home</Link>
      <span> | </span>
      {user ? (
        <button className="btn-ghost btn" onClick={logoutUser}>Logout</button>
      ) : (
        <Link to="/login" className="btn-ghost btn">Login</Link>
      )}

      {user && <p className="ml-auto btn-ghost btn">Hello {user.username}</p>}
    </div>
  );
};

export default Header;
