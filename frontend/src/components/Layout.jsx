import { Link, Outlet } from "react-router-dom";

function Layout() {
  return (
    <div>
      <nav>
        <Link to="/">Home</Link>
        {" | "}
        <Link to="/board">Board</Link>
      </nav>
      <hr />
      <Outlet />
    </div>
  );
}

export default Layout;
