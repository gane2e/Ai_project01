from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
from models import User

# 데이터 유효성 검사를 위한 pydantic 모델 가져오기
from pydantic import BaseModel

# CORS 미들웨어 추가를 위한 모듈 가져오기
from fastapi.middleware.cors import CORSMiddleware

# 데이터베이스에 테이블 생성(이미 존재하면 건너뜀)
Base.metadata.create_all(bind=engine)

# FastAPI 애플리케이션 인스턴스 생성
app = FastAPI()

# pydantic 모델 정의(요청 데이터 유효성 검사)
class UserCreate(BaseModel):
  name:str

# CORS (Cross-Origin Resource Sharing) 설정 추가
# 다른 도메인에서 API 요청을 허용하는 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8081"],  # Vue.js 프론트엔드가 실행되는 주소
    allow_credentials=True,  # 인증 정보(쿠키 등) 허용
    allow_methods=["*"],  # 모든 HTTP 메서드 허용 (GET, POST, PUT, DELETE 등)
    allow_headers=["*"],  # 모든 헤더 허용
)

# 데이터베이스 세션을 제공하는 의존성 함수
def get_db():
  db = SessionLocal() #데이터베이스 세션 생성
  try:
    yield db #호출한 곳에서 세션을 사용할 수 있도록 제공
  finally:
    db.close() #세션 연결 종료

@app.get("/")
def getDefault(db: Session = Depends(get_db)):
  return "Hello, FastAPI";


@app.get("/users/")
def readUser(db: Session = Depends(get_db)):
  return db.query(User).all();

@app.post("/users/")
def createUser(user: UserCreate, db: Session = Depends(get_db)):
  new_user = User(name = user.name)
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user;
