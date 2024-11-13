# matching/utils.py or profiles/utils.py

def calculate_match_score(user_profile, match_profile):
    """
    Calculates a match score based on shared attributes between two profiles.
    
    :param user_profile: Profile of the current user.
    :param match_profile: Profile of the potential match.
    :return: A numeric match score.
    """
    score = 0
    
    # Example criteria and scoring logic
    if user_profile.religion == match_profile.religion:
        score += 10
    if user_profile.caste == match_profile.caste:
        score += 10
    if user_profile.education == match_profile.education:
        score += 10
    if user_profile.profession == match_profile.profession:
        score += 10
    if abs(user_profile.height - match_profile.height) <= 5:
        score += 5
    if abs(user_profile.weight - match_profile.weight) <= 5:
        score += 5
    if user_profile.income == match_profile.income:
        score += 10
    
    return score
