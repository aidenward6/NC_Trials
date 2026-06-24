class Solution:
    def countSeniors(self, details: List[str]) -> int:
        person_count = 0
        for info in details:
            age_str = info[11:13]
            if int(age_str) > 60:
                person_count += 1
        return person_count
            