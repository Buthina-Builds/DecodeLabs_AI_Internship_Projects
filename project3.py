# Project 3: AI Recommendation Logic
# Powered by DecodeLabs

def run_recommendation_engine():
    print("==================================================")
    print("DecodeLabs Content-Based AI Recommendation Engine")
    print("==================================================")
    
    # 1. Intrinsically Defined Item Database (Intrinsic properties mapped to vocabulary)
    items_db = [
        {"title": "Advanced Web Development Course", "tags": ["web design", "frontend", "javascript", "html"]},
        {"title": "Python for Data Science Masterclass", "tags": ["python", "data science", "analytics", "machine learning"]},
        {"title": "AI & Deep Learning Intensive", "tags": ["python", "neural networks", "tensors", "ai", "machine learning"]},
        {"title": "Automated Cloud DevOps Pipeline", "tags": ["cloud", "automation", "devops", "linux"]},
        {"title": "Java Programming & Algorithmic Logic", "tags": ["java", "algorithms", "software development"]}
    ]
    
    available_interests = ["python", "web design", "machine learning", "cloud", "algorithms", "java", "software development"]
    print("Available Interest Tags:")
    print(", ".join(available_interests))
    print("--------------------------------------------------")
  
    user_input = input("Enter your interest tags (separated by commas, e.g., 'python, machine learning'): ")
    user_profile_tags = [tag.strip().lower() for tag in user_input.split(",") if tag.strip()]
    
    print(f"\nUser Profile Vector Activated for Tags: {user_profile_tags}")
    
    # 3. Process: Similarity Logic (Binary Overlap Counter)
    recommendation_scores = []
    
    for item in items_db:
       
        overlap = set(user_profile_tags).intersection(set(item["tags"]))
        score = len(overlap)
        recommendation_scores.append({
            "title": item["title"],
            "score": score,
            "matched_tags": list(overlap)
        })
    
    recommendation_scores.sort(key=lambda x: x["score"], reverse=True)
    
    # 4. Output Generation (Top-N Tailored List)
    print("\n================ TOP RECOMMENDATIONS ================")
    rank = 1
    has_recommendations = False
    
    for rec in recommendation_scores:
        if rec["score"] > 0:
            print(f"{rank}. {rec['title']} (Match Score: {rec['score']} | Matches: {rec['matched_tags']})")
            rank += 1
            has_recommendations = True
            
    if not has_recommendations:
        print("No exact tag alignment found. Try exploring with different keywords like 'python' or 'web design'!")
    print("==================================================")

if __name__ == "__main__":
    run_recommendation_engine()