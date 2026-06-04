from typing import List, Dict, Any



def format_chat_results(points)->List[Dict[str, Any]]:

    results =[]
    for point in points:
        payload = point.payload
        content = payload.get("page_content","")
        metadata = payload.get("metadata", "")

        user_msg =""
        assitant_msg = ""

        if "User:" in content and "Assistant:" in content:
            parts = content.split("Assistant:")
            user_part = parts[0].strip()
            assitant_msg = parts[1].strip() if len(parts)>1 else ""
            user_msg = user_part.replace("User:", "").strip()

        chat_msg = {
            "id": str(point.id),
            "user_message": user_msg,
            "assistant_message": assitant_msg,
            "timestamp": metadata.get("timestamp", ""),
            "user_id": metadata.get("user_id", ""),
            "chat_id": metadata.get("chat_id", "")
        }
        results.append(chat_msg)
    return results