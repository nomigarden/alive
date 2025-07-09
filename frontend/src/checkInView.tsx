import { useEffect, useState } from "react";

const BACKEND_URL = "http://localhost:8000";


export default function CheckinView() {
    const [lastCheckIn, setLastCheckIn] = useState<string | null>(null);
    const [loading, setLoading] = useState(true);
    const [statusMessage, setStatusMessage] = useState("");

    useEffect(() => {
        const fetchLastCheckin = async () => {
            try {
                const res = await fetch(`${BACKEND_URL}/last-checkin`);
                const data = await res.json();
                setLastCheckIn(data.last_checkin);
            } catch (err) {
                setStatusMessage("Error while loading data from server.");
            } finally {
                setLoading(false);
            }
        }
        fetchLastCheckin();
    }, []);

    const handleCheckIn = async () => {
        const now = new Date().toISOString();

        const ip = null;
        const location = null;

        const payload = {
            timestamp: now,
            ip,
            location,
        };

        const res = await fetch(`${BACKEND_URL}/check-in`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload),
        });

        if (res.ok) {
            setLastCheckIn(now);
            setStatusMessage("All ok.");
        } else {
            setStatusMessage("Something went wrong.");
        }
    };

    const formatTimeSince = (isotime: string) => {
        const then = new Date(isotime).getTime();
        const now = Date.now();
        const diffMs = now - then;
        const diffMin = Math.floor(diffMs / 60000);

        if (diffMin < 1) return "less than minute ago";
        if (diffMin < 60) return `less than ${diffMin} minutes ago.`
        const h = Math.floor(diffMin / 60);
        return `${h} hours ago`;
    }

    return (
        <div className="p-6 max-w-md mx-auto bg-zinc-900 text-white rounded-xl shadow-lg space-y-4">
            <h2>PUSH THE BUTTON!!!1</h2>

            {loading ? (
                <p>Loading...</p>
            ) : (
                <p>
                    Last log:{" "}
                    <span className="font-mono">
                        {lastCheckIn ? formatTimeSince(lastCheckIn) : "No logs"}
                    </span>
                </p>
            )}

            <button
                onClick={handleCheckIn}
                className="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded"
            >
                Send ACK
            </button>

            {statusMessage && <p className="text-sm text-emerald-400">{statusMessage}</p>}

        </div>
    );
}