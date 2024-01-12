import connectToMongo from "@/db/page";
import Image from "@/models/images.models";
import { NextResponse } from "next/server";

export async function GET() {
    try {
        await connectToMongo();
        const images = await Image.find();
        return NextResponse.json({images});
    } catch (error) {
        return NextResponse.json({message: "No images found."}, {status: 500});
    }
}

export async function POST(request) {
    try {
        const data = await request.json();
        await connectToMongo();
        await Image.create(data);
        return NextResponse.json({message: "Image Inserted"}, {status: 201});
    } catch (error) {
        return NextResponse.json({message: `${error} Image not inserted.`}, {status: 500});
    }
}