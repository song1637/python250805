import re

def is_valid_email(email):
    # 이메일 유효성 검사용 정규 표현식
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# 테스트할 이메일 주소 목록
test_emails = [
    "user@example.com",           # ✅ 유효
    "john.doe123@mail.co",        # ✅ 유효
    "hello.world@sub.domain.org", # ✅ 유효
    "test_email+spam@gmail.com",  # ✅ 유효
    "invalid-email.com",          # ❌ @ 없음
    "missing@domain",             # ❌ 도메인 끝이 없음
    "bad@domain..com",            # ❌ 도메인에 이중 점
    "user@@example.com",          # ❌ @ 중복
    "user@.com",                  # ❌ 도메인 시작이 점
    "@missinguser.com",          # ❌ 사용자 이름 없음
]

# 이메일 유효성 검사 실행
for email in test_emails:
    if is_valid_email(email):
        print(f"✅ 유효한 이메일: {email}")
    else:
        print(f"❌ 유효하지 않음: {email}")
