import mongoose from "mongoose";

const connectToMongo = async() => {
    try {
        await mongoose.connect(process.env.MONGODB_URI);
    } catch (error) {
        throw new Error(error);
    }
}

export default connectToMongo;