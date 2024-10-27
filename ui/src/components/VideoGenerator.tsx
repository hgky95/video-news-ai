"use client";

import React, { useState } from "react";

const BACKEND_API = process.env.NEXT_PUBLIC_BACKEND_API || "";

export function VideoGenerator() {
  const [prompt, setPrompt] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [videoUrl, setVideoUrl] = useState("");
  const [error, setError] = useState("");

  const handleGenerate = async () => {
    if (!prompt.trim()) return;

    setIsLoading(true);
    setError("");
    setVideoUrl("");

    try {
      const response = await fetch(BACKEND_API, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ prompt: prompt.trim() }),
      });

      if (!response.ok) {
        throw new Error("Failed to generate video");
      }

      const data = await response.json();
      const videoId = data.video_id;
      const fullVideoUrl = `https://youtube.com/shorts/${videoId}`;
      setVideoUrl(fullVideoUrl);
    } catch (err) {
      setError("An error occurred while generating the video" + err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div
      style={{ backgroundColor: "rgb(193, 225, 193)" }}
      className="max-w-2xl mx-auto bg-white rounded-lg shadow-lg p-6"
    >
      <h1 className="text-2xl font-bold mb-6">
        AI-driven news video generator
      </h1>

      <div className="space-y-4">
        <div>
          <label className="block mb-2">Input prompt:</label>
          <input
            type="text"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            className="w-full p-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
            disabled={isLoading}
          />
        </div>

        <button
          onClick={handleGenerate}
          disabled={isLoading || !prompt.trim()}
          className="w-32 bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700 disabled:bg-blue-300 disabled:cursor-not-allowed mx-auto block"
        >
          {isLoading ? "Generating..." : "Generate"}
        </button>

        {error && <div className="text-red-600 text-center mt-4">{error}</div>}

        {videoUrl && !isLoading && (
          <div className="text-center mt-4 space-y-1">
            <div className="text-green-600">Video uploaded successfully!</div>
          </div>
        )}
      </div>
      {isLoading && (
        <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
          <div className="flex flex-col items-center text-white text-xl">
            <svg
              className="animate-spin h-8 w-8 text-white mb-2"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
            >
              <circle
                className="opacity-25"
                cx="12"
                cy="12"
                r="10"
                stroke="currentColor"
                strokeWidth="4"
              ></circle>
              <path
                className="opacity-75"
                fill="currentColor"
                d="M4 12a8 8 0 018-8V0C6.373 0 0 6.373 0 12h4z"
              ></path>
            </svg>
            Generating...
          </div>
        </div>
      )}
    </div>
  );
}

export default VideoGenerator;
