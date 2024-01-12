import connectToMongo from "@/db/page";
import Profile from "@/models/profile.models";
import { NextResponse } from "next/server";


export async function POST(request) {
    try {
        const data = await request.json();
        await connectToMongo();
        await Profile.create(data);
        return NextResponse.json({message: "Profile Created"}, {status: 201});
    } catch (error) {
        return NextResponse.json({message: `${error} :  Profile not inserted.`}, {status: 500});
    }
}