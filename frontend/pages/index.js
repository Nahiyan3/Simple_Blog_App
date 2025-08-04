import Link from "next/link";

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-white px-4">
      <h1 className="text-4xl font-bold mb-8">Welcome to Blog App</h1>

      <div className="flex gap-4">
        <Link href="/login">
          <button className="px-6 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg">
            Login
          </button>
        </Link>

        <Link href="/signup">
          <button className="px-6 py-2 bg-green-600 hover:bg-green-700 text-white rounded-lg">
            Signup
          </button>
        </Link>
      </div>
    </div>
  );
}
