import { useEffect, useState } from "react";

export default function PostsPage() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const res = await fetch("http://localhost:8000/posts");
        if (!res.ok) throw new Error("Failed to fetch posts");
        const data = await res.json();
        setPosts(data);
      } catch (err) {
        console.error("Failed to fetch posts:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchPosts();
  }, []);

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-blue-50 py-8 px-4">
      <div className="max-w-3xl mx-auto">
        <div className="bg-white rounded-2xl shadow-lg p-8">
          <h1 className="text-3xl font-bold text-gray-800 mb-8 text-center">All Blog Posts</h1>

          {loading ? (
            <p className="text-center text-gray-500">Loading...</p>
          ) : posts.length === 0 ? (
            <p className="text-center text-gray-500">No posts available.</p>
          ) : (
            <div className="space-y-6">
              {posts.map((post) => (
                <div
                  key={post.id}
                  className="border border-gray-200 rounded-lg p-6 hover:shadow-md transition duration-200"
                >
                  <h2 className="text-xl font-semibold text-gray-800 mb-3">{post.title}</h2>
                  <p className="text-gray-700 mb-4 leading-relaxed">{post.content}</p>
                  <p className="text-sm text-gray-500">
                    <span className="font-medium">Author:</span> {post.author_name || "Unknown"}
                  </p>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}