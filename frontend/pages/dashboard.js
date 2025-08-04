import Link from "next/link";
import { useEffect, useState } from "react";
import axios from "axios";

export default function Dashboard() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const userId = localStorage.getItem('userId');
        if (userId) {
          const res = await axios.get(`http://localhost:8000/user/${userId}`);
          setUser(res.data);
        }
      } catch (err) {
        console.error("Failed to fetch user:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchUser();
  }, []);

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 via-white to-blue-50 px-4">
      <div className="bg-white w-full max-w-md p-8 rounded-2xl shadow-xl border border-gray-100 text-center">
        <h1 className="text-3xl font-bold text-gray-800 mb-4">Dashboard</h1>

        {loading ? (
          <p className="text-gray-600 text-base mb-6">Loading...</p>
        ) : user ? (
          <p className="text-lg text-gray-700 mb-6">
            Welcome back, <span className="font-semibold text-blue-600">{user.username}</span>!
          </p>
        ) : (
          <p className="text-gray-600 text-base mb-6">Welcome!</p>
        )}

        <div className="flex flex-col sm:flex-row justify-center gap-4">
          <Link href="/create">
            <button className="w-full sm:w-auto px-6 py-3 bg-blue-600 hover:bg-blue-700 text-white rounded-lg font-medium transition duration-200">
              Create Post
            </button>
          </Link>

          <Link href="/posts">
            <button className="w-full sm:w-auto px-6 py-3 bg-green-600 hover:bg-green-700 text-white rounded-lg font-medium transition duration-200">
              View Posts
            </button>
          </Link>
        </div>
      </div>
    </div>
  );
}
