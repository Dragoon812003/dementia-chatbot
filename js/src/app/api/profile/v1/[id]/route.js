import connectToMongo from "@/db/page";
import Profile from "@/models/profile.models";
import { NextResponse } from "next/server";

export async function GET(request, { params }) {
  const { id } = params;
  await connectToMongo();
  try {
    const profile = await Profile.findOne({ _id: id });
    if (!profile) {
      return NextResponse.json({ error: "Profile not found" }, { status: 404 });
    }
    return NextResponse.json({ profile }, { status: 200 });
  } catch (error) {
    return NextResponse.json({ error: `Internal Server Error : ${error}` }, { status: 500 });
  }
}