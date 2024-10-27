"use client";

import dynamic from "next/dynamic";

const VideoGenerator = dynamic(() => import("@/components/VideoGenerator"), {});

export default function Home() {
  return <VideoGenerator />;
}
